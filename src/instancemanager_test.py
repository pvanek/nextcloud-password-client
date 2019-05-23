import logging
import unittest
import pprint
from cryptography.fernet import Fernet


from instancemanager import *

class InstanceManagerTest(unittest.TestCase):

    MASTER_PASS = Fernet.generate_key()
    CONFIG_FILE_NAME = 'test.json'
    DUMMY_INSTANCE = {
        'name': 'foo',
        'url': 'http://localhost',
        'username': 'foobar',
        'password': 'mypass9284*$@%!$)_(*',
        'verifySSL': True
    }

    def setUp(self):
        self.pp = pprint.PrettyPrinter(indent=4)


    def test(self):
        logging.info("load_empty_config key: " + str(self.MASTER_PASS))
        manager = InstanceManager(master_key=self.MASTER_PASS,
                                  config_file_name=self.CONFIG_FILE_NAME)
        self.assertDictEqual(manager.getInstances(), {})

        try:
            os.remove(manager.configLocation())
        except FileNotFoundError:
            pass

        manager.upsertInstance(self.DUMMY_INSTANCE)
        manager.writeConfig()
        self.assertDictEqual(manager.getInstances(), {self.DUMMY_INSTANCE['name']: self.DUMMY_INSTANCE})

        manager.readConfig()
        self.assertDictEqual(manager.getInstances(), {self.DUMMY_INSTANCE['name']: self.DUMMY_INSTANCE})

    def test_keyring(self):
        key = InstanceManager.getStoredKey()
        pprint.pprint(key)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
