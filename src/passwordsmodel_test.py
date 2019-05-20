import sys
import unittest
import pprint
from PySide2.QtCore import QModelIndex
from PySide2.QtWidgets import QApplication

from passwordsmodel import *


TEST_DATA = [
    {
        "label": "QT",
        "password": "foobar",
        "statusCode": "GOOD",
        "url": "https://foo.bar",
        "username": "myuser"
    },
]


class PasswordsModelTest(unittest.TestCase):

    def setUp(self):
        self.pp = pprint.PrettyPrinter(indent=4)
        self.app = QApplication(sys.argv)


    def test_model(self):
        model = PasswordsModel()
        model.setPasswords(TEST_DATA)
        self.assertEqual(model.headerData(1, Qt.Horizontal, Qt.DisplayRole),
                         list(TEST_DATA[0])[1])
        self.assertEqual(model.columnCount(QModelIndex()), len(list(TEST_DATA[0])))
        self.assertEqual(model.data(QModelIndex(), Qt.DisplayRole),
                         None)


if __name__ == '__main__':
    unittest.main()
