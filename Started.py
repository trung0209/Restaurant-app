# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from WindowCode import Order_window, ManagerWindow


class Ui_MainWindow(object):
    def openCustomerWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Order_window.Ui_menu()
        self.ui.setupUi(self.window)
        self.window.show()

    def openManagerWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ManagerWindow.Ui_Manager()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.customerButton = QtWidgets.QPushButton(self.centralwidget)
        self.customerButton.setGeometry(QtCore.QRect(130, 110, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.customerButton.setFont(font)
        self.customerButton.setObjectName("customerButton")
        self.manageButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageButton.setGeometry(QtCore.QRect(130, 320, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.manageButton.setFont(font)
        self.manageButton.setObjectName("manageButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.customerButton.clicked.connect(lambda: self.openCustomerWindow())
        self.customerButton.clicked.connect(lambda: MainWindow.close())
        self.manageButton.clicked.connect(lambda: self.openManagerWindow())
        self.manageButton.clicked.connect(lambda: MainWindow.close())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.customerButton.setText(_translate("MainWindow", "Customer"))
        self.manageButton.setText(_translate("MainWindow", "Manage system"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
