# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(1213, 636)
        self.centralwidget = QtWidgets.QWidget(menu)
        self.centralwidget.setObjectName("centralwidget")
        self.tableOrder = QtWidgets.QTableWidget(self.centralwidget)
        self.tableOrder.setGeometry(QtCore.QRect(580, 30, 301, 461))
        self.tableOrder.setRowCount(2)
        self.tableOrder.setColumnCount(2)
        self.tableOrder.setObjectName("tableOrder")
        self.tableOrder.horizontalHeader().setDefaultSectionSize(140)
        self.order = QtWidgets.QPushButton(self.centralwidget)
        self.order.setGeometry(QtCore.QRect(640, 597, 81, 21))
        self.order.setObjectName("order")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 551, 521))
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setRowCount(17)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.Billing = QtWidgets.QPushButton(self.centralwidget)
        self.Billing.setGeometry(QtCore.QRect(760, 590, 101, 28))
        self.Billing.setObjectName("Billing")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(760, 550, 101, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.Id_name = QtWidgets.QLineEdit(self.centralwidget)
        self.Id_name.setGeometry(QtCore.QRect(640, 550, 81, 22))
        self.Id_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Id_name.setObjectName("Id_name")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 500, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tableOrder_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableOrder_2.setGeometry(QtCore.QRect(890, 30, 301, 461))
        self.tableOrder_2.setRowCount(2)
        self.tableOrder_2.setColumnCount(2)
        self.tableOrder_2.setObjectName("tableOrder_2")
        self.tableOrder_2.horizontalHeader().setDefaultSectionSize(140)

        menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "MainWindow"))
        self.order.setText(_translate("menu", "Order"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.Billing.setText(_translate("menu", "Billing"))
        self.Id_name.setText(_translate("menu", "ID:"))
        self.pushButton.setText(_translate("menu", "Clear Order"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QMainWindow()
    ui = Ui_menu()
    ui.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())
