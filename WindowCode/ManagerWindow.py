from PyQt5 import QtCore, QtGui, QtWidgets

from WindowCode.ModifyTable import Ui_ModifyTable
from WindowCode.TableManager import Ui_TableManger
from WindowCode.MenuModify import Ui_MenuModify

class Ui_Manager(object):
    def setupUi(self, Manager):
        Manager.setObjectName("Manager")
        Manager.resize(354, 589)
        self.centralwidget = QtWidgets.QWidget(Manager)
        self.centralwidget.setObjectName("centralwidget")
        self.TableCheck = QtWidgets.QPushButton(self.centralwidget)
        self.TableCheck.setGeometry(QtCore.QRect(70, 390, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TableCheck.setFont(font)
        self.TableCheck.setObjectName("TableCheck")
        self.modifyMenu = QtWidgets.QPushButton(self.centralwidget)
        self.modifyMenu.setGeometry(QtCore.QRect(70, 130, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.modifyMenu.setFont(font)
        self.modifyMenu.setObjectName("modifyMenu")
        self.ModifyTable = QtWidgets.QPushButton(self.centralwidget)
        self.ModifyTable.setGeometry(QtCore.QRect(70, 250, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ModifyTable.setFont(font)
        self.ModifyTable.setObjectName("ModifyTable")
        Manager.setCentralWidget(self.centralwidget)

        self.TableCheck.clicked.connect(lambda: self.openTableManager())
        self.ModifyTable.clicked.connect(lambda: self.openTableModify())
        self.modifyMenu.clicked.connect(lambda: self.openMenuModify())

        self.TableCheck.clicked.connect(lambda: Manager.close())
        self.retranslateUi(Manager)
        QtCore.QMetaObject.connectSlotsByName(Manager)

    def openTableManager(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TableManger()
        self.ui.setupUi(self.window)
        self.window.show()

    def openTableModify(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ModifyTable()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMenuModify(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MenuModify()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Manager):
        _translate = QtCore.QCoreApplication.translate
        Manager.setWindowTitle(_translate("Manager", "Manager"))
        self.TableCheck.setText(_translate("Manager", "Manage Table"))
        self.modifyMenu.setText(_translate("Manager", "Modify Menu"))
        self.ModifyTable.setText(_translate("Manager", "Modify Table"))