import copy
from PySide2.QtWidgets import QDialog, QMessageBox
from generated.ui_preferencesdialog import Ui_PreferencesDialog

from nextcloudinstance import NextcloudInstance


class PreferencesDialog(QDialog):
    def __init__(self, instances, *args):
        QDialog.__init__(self, *args)
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)

        self.instances = copy.deepcopy(instances)

        self.updateInstanceList()

        self.ui.addInstanceButton.clicked.connect(self.addInstance)
        self.ui.deteleInstanceButton.clicked.connect(self.deleteInstance)
        self.ui.instancesListWidget.currentRowChanged.connect(
                self.currentInstanceChanged)
        self.ui.testButton.clicked.connect(self.testInstance)
        self.ui.confirmButton.clicked.connect(self.confirmInstance)

    def getInstances(self):
        return self.instances

    def updateInstanceList(self):
        self.ui.instancesListWidget.blockSignals(True)
        self.ui.instancesListWidget.clear()
        for i in self.instances.keys():
            self.ui.instancesListWidget.addItem(i)
        self.ui.instancesListWidget.blockSignals(False)

    def addInstance(self):
        self.clearForm()

    def deleteInstance(self):
        row = self.ui.instancesListWidget.currentRow()
        key = self.ui.instancesListWidget.item(row).text()
        if key:
            self.clearForm()
            del self.instances[key]
            self.ui.instancesListWidget.takeItem(row)

    def clearForm(self):
        self.ui.nameLabel.setEnabled(True)
        self.ui.nameEdit.setEnabled(True)
        self.ui.nameEdit.clear()
        self.ui.urlEdit.clear()
        self.ui.usernameEdit.clear()
        self.ui.passwordEdit.clear()
        self.ui.validateSslCheckBox.setChecked(True)

    def currentInstanceChanged(self, row):
        self.clearForm()
        key = self.ui.instancesListWidget.item(row).text()
        self.ui.nameEdit.setEnabled(False)
        self.ui.nameLabel.setEnabled(False)

        self.ui.nameEdit.setText(self.instances[key]['name'])
        self.ui.urlEdit.setText(self.instances[key]['url'])
        self.ui.usernameEdit.setText(self.instances[key]['username'])
        self.ui.passwordEdit.setText(self.instances[key]['password'])
        self.ui.validateSslCheckBox.setChecked(
                self.instances[key]['verifySSL'])

    def testInstance(self):
        name = self.ui.nameEdit.text()
        verify_ssl = self.ui.validateSslCheckBox.isChecked()
        net = NextcloudInstance(description=name,
                                url=self.ui.urlEdit.text(),
                                username=self.ui.usernameEdit.text(),
                                password=self.ui.passwordEdit.text(),
                                verifySSL=verify_ssl)
        try:
            net.getFolders()
            QMessageBox.information(self, 'Network result',
                                    'Ping to ' + name + ' is OK')
        except Exception as err:
            QMessageBox.warning(self, 'Network result',
                                'Error: ' + format(err))

    def confirmInstance(self):
        name = self.ui.nameEdit.text()

        self.instances[name] = {
            'name': name,
            'url': self.ui.urlEdit.text(),
            'username': self.ui.usernameEdit.text(),
            'password': self.ui.passwordEdit.text(),
            'verifySSL': self.ui.validateSslCheckBox.isChecked()
        }

        self.clearForm()
        self.updateInstanceList()
