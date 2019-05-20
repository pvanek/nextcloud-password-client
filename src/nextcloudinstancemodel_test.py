import sys
import unittest
import pprint
from PySide2.QtWidgets import QApplication

from nextcloudinstancemodel import *

""" a fake NextcloudInstance class for unit test only
"""
class NextcloudInstance:
    def __init__(self):
        self.description = "a test"

    def getFoldersTree(self):
        return [
               {
                   'children': [
                        {
                            'children': [
                                {
                                    'created': 1556876304,
                                    'cseType': 'none',
                                    'edited': 1556876304,
                                    'favorite': False,
                                    'hidden': False,
                                    'id': 'a533bf4f-4b03-48e7-866b-abe09ace3254',
                                    'label': 'test1',
                                    'parent': '4f157ed1-b2d8-4f36-addf-c213cbc7d514',
                                    'revision': 'd0998d17-d2d7-4707-8c9c-ef66b677d0c3',
                                    'sseType': 'SSEv1r1',
                                    'trashed': False,
                                    'updated': 1556876304
                                }
                            ],
                            'created': 1556797672,
                            'cseType': 'none',
                            'edited': 1556797672,
                            'favorite': False,
                            'hidden': False,
                            'id': '4f157ed1-b2d8-4f36-addf-c213cbc7d514',
                            'label': 'test',
                            'parent': '00000000-0000-0000-0000-000000000000',
                            'revision': 'b60f6743-ede5-4a2b-8de3-8e63b2d86942',
                            'sseType': 'SSEv1r1',
                            'trashed': False,
                            'updated': 1556797672
                        }
                    ],
                    'id': '00000000-0000-0000-0000-000000000000',
                    'label': 'mydomain.org',
                    'parent': '-1'
                }
            ]

    def getPasswordsForFolderId(self, folder_id):
        pass


class NextcloudInstanceModelTest(unittest.TestCase):

    def setUp(self):
        self.pp = pprint.PrettyPrinter(indent=4)

        self.app = QApplication(sys.argv)


    def test_model(self):
        instance = NextcloudInstance()
        model = NCTreeModel([instance])
        self.assertEqual(model.headerData(1, Qt.Horizontal, Qt.DisplayRole),
                         "Nextcloud Instances")
        self.assertEqual(model.columnCount(QModelIndex()), 1)
        self.assertEqual(model.data(QModelIndex(), Qt.DisplayRole),
                         None)


if __name__ == '__main__':
    unittest.main()
