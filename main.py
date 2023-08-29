from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import MainWindow
import sys
import json

if __name__ == "__main__":
    try:
        with open('test01\config\config.json', 'r', encoding='utf-8-sig') as file:
            pass
    except FileNotFoundError:
        pass
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
