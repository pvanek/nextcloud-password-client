import keyring
from cryptography.fernet import Fernet
import appdirs
import json
import os
import logging
import copy


class InstanceManager:

    APP_NAME = 'nextcloud-password-client'

    def __init__(self, master_key, config_file_name='nextcloud.json'):
        self.instances = {}
        self.config_file_name = config_file_name
        self.crypto = Fernet(master_key)

    def configLocation(self):
        datadir = appdirs.user_config_dir(self.APP_NAME)
        logging.info('config path ' + datadir)
        if not os.path.exists(datadir):
            logging.info('creating config path ' + datadir)
            os.makedirs(datadir)
        return os.path.join(datadir, self.config_file_name)

    def readConfig(self):
        configpath = self.configLocation()
        if not os.path.isfile(configpath):
            return
        with open(configpath) as f:
            self.instances = json.load(f)
            for i in self.instances:
                val = self.decryptValue(self.instances[i]['password'])
                self.instances[i]['password'] = val
                if 'verifySSL' not in self.instances[i]:
                    self.instances[i]['verifySSL'] = True
        print(self.instances)

    def writeConfig(self):
        configpath = self.configLocation()
        cfg = copy.deepcopy(self.instances)
        with open(configpath, 'w') as f:
            for i in self.instances:
                cfg[i]['password'] = self.encryptValue(cfg[i]['password'])
            json.dump(cfg, f, indent=4)

    def getInstances(self):
        return self.instances

    def upsertInstance(self, config):
        self.instances[config['name']] = config

    def deleteInstance(self, config):
        del self.instances[config['name']]

    def replaceInstances(self, config):
        self.instances = config

    def encryptValue(self, value):
        v = self.crypto.encrypt(value.encode('utf-8'))
        ret = v.decode('ascii')
        return ret

    def decryptValue(self, value):
        ret = self.crypto.decrypt(value.encode()).decode('utf-8')
        return ret

    @staticmethod
    def getStoredKey():
        key = keyring.get_password(InstanceManager.APP_NAME, 'master_key')
        if not key:
            key = Fernet.generate_key()
            keyring.set_password(InstanceManager.APP_NAME,
                                 'master_key',
                                 key.decode('utf-8'))
            # re-read the key in encoded form
            key = keyring.get_password(InstanceManager.APP_NAME, 'master_key')
        return key.encode('utf-8')
