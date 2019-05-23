import unittest
import pprint
import os
from json.decoder import JSONDecodeError
from nextcloudinstance import NextcloudInstance

class NextcloudInstanceTest(unittest.TestCase):

    def setUp(self):
        self.pp = pprint.PrettyPrinter(indent=4)

        self.nextcloud = NextcloudInstance(username=os.environ['TEST_USERNAME'],
                                           password=os.environ['TEST_PASSWORD'],
                                           url=os.environ['TEST_URL'],
                                           description='test instance',
                                           verifySSL=True)

    def test_get(self):
        resp = self.nextcloud.get('foobar')
        with self.assertRaises(JSONDecodeError):
            resp.json()


    def test_getFolders(self):
        folders = self.nextcloud.getFolders()
        self.assertTrue(type(folders) is list)
        for i in folders:
            self.assertTrue('id' in i)
            self.assertTrue('label' in i)
            self.assertTrue('parent' in i)


    def test_getPasswords(self):
        passwords = self.nextcloud.getPasswords()
        self.assertTrue(type(passwords) is list)
        for i in passwords:
            self.assertTrue('id' in i)
            self.assertTrue('label' in i)
            self.assertTrue('username' in i)
            self.assertTrue('password' in i)
            self.assertTrue('folder' in i)


    def test_getFoldersTree(self):
        tree = self.nextcloud.getFoldersTree()
        self.pp.pprint(tree)
        self.assertTrue(type(tree) is list)


    def test_getPasswordsForFolderId(self):
        folders = self.nextcloud.getFolders()
        folders.append({'id': NextcloudInstance.root_id})
        for i in (folders):
             passwords = self.nextcloud.getPasswordsForFolderId(i['id'])
             self.assertTrue(type(passwords) is list)
             #self.pp.pprint(passwords)


if __name__ == '__main__':
    unittest.main()

