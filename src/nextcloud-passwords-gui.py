import sys
import logging
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon
from mainwindow import MainWindow
import generated.icons


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info('started')

    QApplication.setApplicationName('Nextcloud Password Client')

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon.fromTheme('dialog-password',
                                      QIcon(':/icons/dialog-password.svg')))
    m = MainWindow()
    m.show()

    rc = app.exec_()

    logging.info('finished')
    sys.exit(rc)
