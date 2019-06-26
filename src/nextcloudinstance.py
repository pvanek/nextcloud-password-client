import logging
import requests
from urllib.parse import urljoin


class NextcloudInstance:

    root_id = '00000000-0000-0000-0000-000000000000'

    def __init__(self, description, url, username, password, verifySSL):
        logging.debug('NextcloudInstance creation: ' + description)
        self.description = description
        self.url = urljoin(url, '/index.php/apps/passwords/api/1.0/')
        self.username = username
        self.password = password
        self.verifySSL = verifySSL

        self.clear()

    def clear(self):
        self.folder_cache = None
        self.password_cache = None

    def get(self, api_url):
        logging.debug('NextcloudInstance.get: ' + api_url)
        resp = requests.get(urljoin(self.url, api_url),
                            auth=(self.username, self.password),
                            verify=self.verifySSL,
                            )
        if (resp.status_code != 200):
            logging.warning('NextcloudInstance.get: ConnectionError = '
                            + str(resp.status_code) + " " + resp.text)
            raise ConnectionError('HTTP status code = '
                                  + str(resp.status_code)
                                  + "; " + resp.text)

        return resp

    def post(self, api_url, body):
        logging.debug('NextcloudInstance.post: ' + api_url
                      + '; body: ' + str(body))
        resp = requests.post(urljoin(self.url, api_url),
                             auth=(self.username, self.password),
                             verify=self.verifySSL,
                             data=body)
        if (resp.status_code != 200):
            logging.warning('NextcloudInstance.get: ConnectionError = '
                            + str(resp.status_code) + " " + resp.text)
            raise ConnectionError('HTTP status code = '
                                  + str(resp.status_code)
                                  + "; " + resp.text)

        return resp

    def getFolders(self):
        logging.debug('NextcloudInstance.getFolders called')
        if (not self.folder_cache):
            self.folder_cache = self.get('folder/list').json()
        else:
            logging.debug('NextcloudInstance.getFolders cache hit')
        return self.folder_cache

    def getPasswords(self):
        logging.debug('NextcloudInstance.getPasswords called')
        if (not self.password_cache):
            body = {"details": "model+revisions+folder+tags+shares"}
            self.password_cache = self.post('password/list', body).json()
        else:
            logging.debug('NextcloudInstance.getPasswords cache hit')
        return self.password_cache

    def getFoldersTree(self):
        logging.debug('NextcloudInstance.getFoldersTree called')
        root = '-1'
        raw_nodes = self.getFolders()
        # append a fake root folder
        raw_nodes.append({'id': self.root_id, 'parent': root, 'label': 'root'})

        nodes = {}
        for i in raw_nodes:
            id, obj = (i['id'], i)
            nodes[id] = obj

        forest = []
        for i in raw_nodes:
            id, parent_id, obj = (i['id'], i['parent'], i)
            node = nodes[id]

            if parent_id == root:
                forest.append(node)
            else:
                parent = nodes[parent_id]
                if 'children' not in parent:
                    parent['children'] = []
                parent['children'].append(node)

        return forest

    def getPasswordsForFolderId(self, folder_id):
        logging.debug('NextcloudInstance.getPasswordsForFolderId called: '
                      + folder_id)
        passwords = self.getPasswords()
        ret = []
        for i in passwords:
            if i['folder']['id'] == folder_id:
                ret.append(i)
        return ret
