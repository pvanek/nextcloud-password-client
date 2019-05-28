import logging

from PySide2.QtCore import Qt, QAbstractItemModel, QModelIndex
from PySide2.QtGui import QIcon

import generated.icons

class NCTreeItemBase(object):
    def __init__(self, parent=None):
        self.parentItem = parent
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return 1

    def displayText(self):
        raise ValueError('no text to display in NCTreeItemBase')

    def displayIcon(self):
        raise ValueError('no icon to display in NCTreeItemBase')

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0

    def getPasswords(self):
        raise ValueError('cannot get passwirds for this item')


class NCRootTreeItem(NCTreeItemBase):
    def __init__(self, header):
        super(NCRootTreeItem, self).__init__(None)
        self.header = header

    def displayText(self):
        return self.header


class NCServerTreeItem(NCTreeItemBase):
    def __init__(self, ncInstance, parent=None):
        super(NCServerTreeItem, self).__init__(parent)
        self.ncInstance = ncInstance

    def displayText(self):
        return self.ncInstance.description

    def displayIcon(self):
        return QIcon.fromTheme('network-server', QIcon(':/icons/network-server.svg'))

    def setupModelData(self):
        try:
            for i in self.ncInstance.getFoldersTree():
                self.addItem(i, self)
        except Exception as err:
            logging.warning(format(err))

    def addItem(self, itemData, parentItem):
        item = NCFolderTreeItem(self.ncInstance, itemData, parentItem)
        parentItem.appendChild(item)
        if 'children' in itemData:
            for i in itemData['children']:
                self.addItem(i, item)

    def getPasswords(self):
        return self.ncInstance.getPasswords()


class NCFolderTreeItem(NCTreeItemBase):
    def __init__(self, ncInstance, itemData, parent=None):
        super(NCFolderTreeItem, self).__init__(parent)
        self.ncInstance = ncInstance
        self.itemData = itemData

    def displayText(self):
        return self.itemData['label']

    def displayIcon(self):
        return QIcon.fromTheme('folder', QIcon(':/icons/folder.svg'))

    def getPasswords(self):
        return self.ncInstance.getPasswordsForFolderId(self.itemData['id'])


class NCTreeModel(QAbstractItemModel):
    def __init__(self, ncInstanceList, parent=None):
        super(NCTreeModel, self).__init__(parent=parent)

        self.ncInstanceList = ncInstanceList
        self.rootItem = NCRootTreeItem(self.tr("Nextcloud Instances"))
        self.setupModelData()

    def setupModelData(self):
        for i in self.ncInstanceList:
            item = NCServerTreeItem(i, self.rootItem)
            item.setupModelData()
            self.rootItem.appendChild(item)

    def getPasswords(self, index):
        if not index.isValid():
            return None

        item = index.internalPointer()
        return item.getPasswords()

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == Qt.DisplayRole:
            return item.displayText()
        if role == Qt.DecorationRole:
            return item.displayIcon()

        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.displayText()

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()
