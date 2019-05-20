import logging
import requests
from urllib.parse import urljoin

class NextcloudInstance:

    root_id = '00000000-0000-0000-0000-000000000000'

    def __init__(self, description, url, username, password):
        logging.debug('NextcloudInstance creation: ' + description)
        self.description = description
        self.url = urljoin(url, '/index.php/apps/passwords/api/1.0/')
        self.username = username
        self.password = password

        self.clear()


    def clear(self):
        self.folder_cache = None
        self.password_cache = None


    def get(self, api_url):
        logging.debug('NextcloudInstance.get: ' + api_url)
        resp = requests.get(urljoin(self.url, api_url),
                            auth=(self.username, self.password))
        if (resp.status_code != 200):
            logging.warning('NextcloudInstance.get: ConnectionError = ' + resp.status_code)
            raise ConnectionError('HTTP status code = ' + resp.status_code)

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
            self.password_cache = self.get('password/list').json()
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
                if not 'children' in parent:
                    parent['children'] = []
                parent['children'].append(node)

        return forest


    def getPasswordsForFolderId(self, folder_id):
        logging.debug('NextcloudInstance.getPasswordsForFolderId called: ' + folder_id)
        passwords = self.getPasswords()
        ret = []
        for i in passwords:
            if i['folder'] == folder_id:
                ret.append(i)
        return ret