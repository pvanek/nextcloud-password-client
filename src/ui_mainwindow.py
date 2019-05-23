# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Thu May 23 10:23:54 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(828, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.treeView = QtWidgets.QTreeView(self.splitter_2)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setObjectName("treeView")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableView = QtWidgets.QTableView(self.splitter)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName("tableView")
        self.detailTabWidget = QtWidgets.QTabWidget(self.splitter)
        self.detailTabWidget.setObjectName("detailTabWidget")
        self.tabDetails = QtWidgets.QWidget()
        self.tabDetails.setObjectName("tabDetails")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabDetails)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.detailsBrowser = QtWidgets.QTextBrowser(self.tabDetails)
        self.detailsBrowser.setObjectName("detailsBrowser")
        self.gridLayout_3.addWidget(self.detailsBrowser, 0, 0, 1, 1)
        self.detailTabWidget.addTab(self.tabDetails, "")
        self.tabNotes = QtWidgets.QWidget()
        self.tabNotes.setObjectName("tabNotes")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabNotes)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.notesBrowser = QtWidgets.QTextBrowser(self.tabNotes)
        self.notesBrowser.setObjectName("notesBrowser")
        self.gridLayout_4.addWidget(self.notesBrowser, 0, 0, 1, 1)
        self.detailTabWidget.addTab(self.tabNotes, "")
        self.tabRevisions = QtWidgets.QWidget()
        self.tabRevisions.setObjectName("tabRevisions")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabRevisions)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.revisionsBrowser = QtWidgets.QTextBrowser(self.tabRevisions)
        self.revisionsBrowser.setObjectName("revisionsBrowser")
        self.gridLayout_5.addWidget(self.revisionsBrowser, 0, 0, 1, 1)
        self.detailTabWidget.addTab(self.tabRevisions, "")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 27))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.menu_File.addAction(self.actionRefresh)
        self.menu_File.addAction(self.actionPreferences)
        self.menu_File.addAction(self.actionQuit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        self.detailTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Nextcloud Passwords", None, -1))
        self.detailTabWidget.setTabText(self.detailTabWidget.indexOf(self.tabDetails), QtWidgets.QApplication.translate("MainWindow", "Details", None, -1))
        self.detailTabWidget.setTabText(self.detailTabWidget.indexOf(self.tabNotes), QtWidgets.QApplication.translate("MainWindow", "Notes", None, -1))
        self.detailTabWidget.setTabText(self.detailTabWidget.indexOf(self.tabRevisions), QtWidgets.QApplication.translate("MainWindow", "Revisions", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.actionPreferences.setText(QtWidgets.QApplication.translate("MainWindow", "&Preferences...", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "&Quit", None, -1))
        self.actionRefresh.setText(QtWidgets.QApplication.translate("MainWindow", "&Refresh", None, -1))

