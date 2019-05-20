import logging
from PySide2.QtCore import QAbstractTableModel, Qt

"""
    {
        "created": 1556793540,
        "cseType": "none",
        "customFields": "[]",
        "editable": true,
        "edited": 1556793540,
        "favorite": false,
        "folder": "00000000-0000-0000-0000-000000000000",
        "hash": "874244cdaa3d93e3bc7cfb884851f0ad07ae2137",
        "hidden": false,
        "id": "dcaf1865-54b1-4771-99c3-fb38905b4847",
        "label": "QT",
        "notes": "",
        "password": "mypass",
        "revision": "225b82d5-52ad-454b-9b39-4bade357cc24",
        "share": null,
        "sseType": "SSEv1r1",
        "status": 0,
        "statusCode": "GOOD",
        "trashed": false,
        "updated": 1556793540,
        "url": "https://bugs.qoretechnologies.com",
        "username": "xxxusername"
    },
"""

VALID_KEYS = [
    'label',
    'url',
    'username',
    'password',
    'statusCode',
]

class PasswordsModel(QAbstractTableModel):
    def __init__(self, parent=None):
        logging.debug('PasswordsModel')
        super(PasswordsModel, self).__init__(parent=parent)
        self.setPasswords()

    def setPasswords(self, passwordsList=[]):
        logging.debug('PasswordsModel.setPasswords called: ' + str(len(passwordsList)))
        self.beginResetModel()
        self.modelData = []
        for i in passwordsList:
            self.modelData.append({k:v for k, v in i.items() if k in VALID_KEYS})
        self.endResetModel()
        logging.debug('PasswordsModel.setPasswords end: ' + str(len(passwordsList)))

    def columnCount(self, parent):
        if len(self.modelData):
            logging.debug('PasswordsModel.columnCount: ' + str(len(self.modelData[0])))
            return len(self.modelData[0])
        else:
            logging.debug('PasswordsModel.columnCount: ' + str(0))
            return 0

    def rowCount(self, parent):
        logging.debug('PasswordsModel.rowCount: ' + str(len(self.modelData)))
        return len(self.modelData)

    def data(self, index, role):
        logging.debug('PasswordsModel.data: ' + str(index.isValid()))
        if not index.isValid():
            return None
        row = index.row()
        column = index.column()

        if role == Qt.DisplayRole:
            return list(self.modelData[row].values())[column]

        return None

    def flags(self, index):
        logging.debug('PasswordsModel.flags called')
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        logging.debug('PasswordsModel.headerData: ' + str(section))
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return list(self.modelData[0])[section]

        return None


