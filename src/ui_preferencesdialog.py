# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferencesdialog.ui',
# licensing of 'preferencesdialog.ui' applies.
#
# Created: Thu May 23 09:22:15 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(412, 325)
        self.gridLayout_2 = QtWidgets.QGridLayout(PreferencesDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(PreferencesDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.instancesListWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.instancesListWidget.setObjectName("instancesListWidget")
        self.verticalLayout.addWidget(self.instancesListWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addInstanceButton = QtWidgets.QToolButton(self.layoutWidget)
        self.addInstanceButton.setObjectName("addInstanceButton")
        self.horizontalLayout.addWidget(self.addInstanceButton)
        self.deteleInstanceButton = QtWidgets.QToolButton(self.layoutWidget)
        self.deteleInstanceButton.setObjectName("deteleInstanceButton")
        self.horizontalLayout.addWidget(self.deteleInstanceButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 2)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 2, 1, 1)
        self.urlLabel = QtWidgets.QLabel(self.groupBox)
        self.urlLabel.setObjectName("urlLabel")
        self.gridLayout.addWidget(self.urlLabel, 1, 0, 1, 1)
        self.urlEdit = QtWidgets.QLineEdit(self.groupBox)
        self.urlEdit.setObjectName("urlEdit")
        self.gridLayout.addWidget(self.urlEdit, 1, 2, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(self.groupBox)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 2, 0, 1, 2)
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 3, 2, 1, 1)
        self.usernameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.usernameEdit.setObjectName("usernameEdit")
        self.gridLayout.addWidget(self.usernameEdit, 2, 2, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.groupBox)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 3, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.testButton = QtWidgets.QPushButton(self.groupBox)
        self.testButton.setObjectName("testButton")
        self.horizontalLayout_2.addWidget(self.testButton)
        self.confirmButton = QtWidgets.QPushButton(self.groupBox)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_2.addWidget(self.confirmButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 2)
        self.validateSslCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.validateSslCheckBox.setChecked(True)
        self.validateSslCheckBox.setObjectName("validateSslCheckBox")
        self.gridLayout.addWidget(self.validateSslCheckBox, 4, 0, 1, 3)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(PreferencesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), PreferencesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), PreferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QtWidgets.QApplication.translate("PreferencesDialog", "Dialog", None, -1))
        self.addInstanceButton.setText(QtWidgets.QApplication.translate("PreferencesDialog", "+", None, -1))
        self.deteleInstanceButton.setText(QtWidgets.QApplication.translate("PreferencesDialog", "-", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("PreferencesDialog", "Nextcloud Instance", None, -1))
        self.nameLabel.setText(QtWidgets.QApplication.translate("PreferencesDialog", "Name", None, -1))
        self.nameEdit.setPlaceholderText(QtWidgets.QApplication.translate("PreferencesDialog", "Type instance name", None, -1))
        self.urlLabel.setText(QtWidgets.QApplication.translate("PreferencesDialog", "Url", None, -1))
        self.urlEdit.setPlaceholderText(QtWidgets.QApplication.translate("PreferencesDialog", "Nextcloud base URL", None, -1))
        self.usernameLabel.setText(QtWidgets.QApplication.translate("PreferencesDialog", "Username", None, -1))
        self.usernameEdit.setPlaceholderText(QtWidgets.QApplication.translate("PreferencesDialog", "User name", None, -1))
        self.passwordLabel.setText(QtWidgets.QApplication.translate("PreferencesDialog", "Password", None, -1))
        self.testButton.setText(QtWidgets.QApplication.translate("PreferencesDialog", "Test", None, -1))
        self.confirmButton.setText(QtWidgets.QApplication.translate("PreferencesDialog", "Done", None, -1))
        self.validateSslCheckBox.setText(QtWidgets.QApplication.translate("PreferencesDialog", "Validate SSL", None, -1))

