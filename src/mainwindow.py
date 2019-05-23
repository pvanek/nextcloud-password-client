import logging
from PySide2.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu
from PySide2.QtGui import QIcon
from PySide2.QtCore import Slot, QModelIndex
from ui_mainwindow import Ui_MainWindow
from nextcloudinstancemodel import NCTreeModel
from nextcloudinstance import NextcloudInstance
from passwordsmodel import PasswordsModel
from instancemanager import InstanceManager
from preferencesdialog import PreferencesDialog


class MainWindow(QMainWindow):
    def __init__(self, *args):
        logging.debug('MainWindow creation')

        QMainWindow.__init__(self, *args)
        self.ui = Ui_MainWindow()
        logging.debug('MainWindow ui setup')
        self.ui.setupUi(self)

        self.instanceManager = InstanceManager(InstanceManager.getStoredKey())
        self.readConfig()
        self.setupModels()

        self.ui.treeView.activated.connect(self.updatePasswordsModel)
        self.ui.tableView.activated.connect(self.udpateDetailTabs)
        self.ui.actionQuit.triggered.connect(self.closeReally)
        self.ui.actionPreferences.triggered.connect(self.openPreferences)
        self.ui.actionRefresh.triggered.connect(self.refreshInstances)

        # Init QSystemTrayIcon
        self.trayIcon = QSystemTrayIcon(QIcon.fromTheme('dialog-password'), self)
        systrayMenu = QMenu(self)
        systrayMenu.addAction(self.ui.actionRefresh)
        systrayMenu.addAction(self.ui.actionQuit)
        self.trayIcon.setContextMenu(systrayMenu)
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.handleSystray)


    # close to systray
    def closeEvent(self, event):
        event.ignore()
        self.hide()


    # close by Quit action
    def closeReally(self):
        exit(0)


    def handleSystray(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()


    @Slot(QModelIndex)
    def updatePasswordsModel(self, index):
        logging.debug('MainWindow.updatePasswordsModel called')
        passwords = self.treeModel.getPasswords(index)
        self.listModel.setPasswords(passwords)


    def udpateDetailTabs(self, index):
        logging.debug('MainWindow.udpateDetailTabs called')
        password = self.listModel.getPassword(index.row())

        self.ui.detailTabWidget.setVisible(True)
        self.ui.detailTabWidget.setCurrentIndex(0);

        if 'notes' in password:
            self.ui.notesBrowser.setText(password['notes'])
            self.ui.tabNotes.setEnabled(True)
        else:
            self.ui.tabNotes.setEnabled(False)

        if 'revisions' in password:
            for i in password['revisions']:
                for key, val in i.items():
                    self.ui.revisionsBrowser.append(key + ': ' + str(val))
                self.ui.revisionsBrowser.append('\n')
            self.ui.tabRevisions.setEnabled(True)
        else:
            self.ui.tabRevisions.setEnabled(False)

        self.ui.detailsBrowser.clear()
        for key, val in password.items():
            if key not in ['notes', 'revisions']:
                self.ui.detailsBrowser.append(key + ': ' + str(val))


    def readConfig(self):
        self.ncInstances = []
        self.instanceManager.readConfig()
        for i, val in self.instanceManager.getInstances().items():
            logging.debug('reading: ' + i)
            self.ncInstances.append(NextcloudInstance(description=val['name'],
                                                      url=val['url'],
                                                      username=val['username'],
                                                      password=val['password'],
                                                      verifySSL=val['verifySSL']
                                                     )
                                   )


    def setupModels(self):
        self.ui.treeView.blockSignals(True)

        self.ui.detailTabWidget.setVisible(False)

        self.treeModel = NCTreeModel(self.ncInstances, self)
        self.listModel = PasswordsModel(self)
        self.ui.treeView.setModel(self.treeModel)

        self.ui.treeView.blockSignals(False)

        self.ui.tableView.setModel(self.listModel)


    def openPreferences(self):
        dia = PreferencesDialog(self.instanceManager.getInstances())
        if (dia.exec_()):
            self.instanceManager.replaceInstances(dia.getInstances())
            self.instanceManager.writeConfig()
            self.refreshInstances()


    def refreshInstances(self):
        self.readConfig()
        self.setupModels()