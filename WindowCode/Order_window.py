# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
from random import randint

from WindowCode import message

from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QPushButton
from WindowCode.Order import Order_list
from WindowCode.Billing_window import Ui_BillWindow

menuDict = { "fish": 23.9,
             "chicken": 19.9,
             "dragon": 10000000,
             "kimchi": 10000000000 }  # temporary menu

from PyQt5 import QtCore, QtWidgets

def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

class Ui_menu(object):
    def __init__(self):
        self.menu_list = { }
        filePath = r"C:\Users\Asus\Documents\Restaurant\Menu\Menu.txt"
        f = open(filePath, "r")
        for x in f:
            temp = x.split(":")
            self.menu_list[temp[0]] = int(temp[1])
        f.close()
        id = random_with_N_digits(6)
        self.order1 = Order_list(id)  # Order of a table with ID
        self.current_order = { }
        # self.menu_list = menuDict

    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(919, 637)
        self.centralwidget = QtWidgets.QWidget(menu)
        self.centralwidget.setObjectName("centralwidget")
        self.tableOrder = QtWidgets.QTableWidget(self.centralwidget)
        self.tableOrder.setGeometry(QtCore.QRect(590, 30, 321, 461))
        self.tableOrder.setRowCount(2)
        self.tableOrder.setColumnCount(2)
        self.tableOrder.setObjectName("tableOrder")
        self.tableOrder.horizontalHeader().setDefaultSectionSize(150)
        self.order = QtWidgets.QPushButton(self.centralwidget)
        self.order.setGeometry(QtCore.QRect(660, 590, 93, 28))
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(132)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.Billing = QtWidgets.QPushButton(self.centralwidget)
        self.Billing.setGeometry(QtCore.QRect(780, 590, 93, 28))
        self.Billing.setObjectName("Billing")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(770, 550, 101, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.Id_name = QtWidgets.QLineEdit(self.centralwidget)
        self.Id_name.setGeometry(QtCore.QRect(660, 550, 81, 22))
        self.Id_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Id_name.setObjectName("Id_name")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 500, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tableOrder.raise_()
        self.order.raise_()
        self.Billing.raise_()
        self.tableWidget.raise_()
        self.lineEdit.raise_()
        self.Id_name.raise_()
        self.pushButton.raise_()
        menu.setCentralWidget(self.centralwidget)

        self.lineEdit.setText(str(self.order1.get_id()))

        self.tableWidget.setRowCount(len(self.menu_list.keys()) + 1)
        self.tableWidget.setColumnCount(4)

        row = 0  # Index of menu table widget

        for key, value in self.menu_list.items():

            if row > len(self.menu_list.keys()):
                break

            item = QTableWidgetItem(key)
            item2 = QTableWidgetItem(str(value)+"₩")
            self.tableWidget.setItem(row, 0, item)
            self.tableWidget.setItem(row, 1, item2)

            self.btn_sell = QPushButton('Add')
            self.btn_sell.clicked.connect(lambda: self.add())
            self.tableWidget.setCellWidget(row, 3, self.btn_sell)
            row += 1

        self.tableWidget.setHorizontalHeaderLabels(["Name", "Price", "Number of dish", "Add to order"])

        self.order_row = 0
        # self.state = False

        self.tableOrder.setRowCount(3)
        self.tableOrder.setColumnCount(2)
        self.tableOrder.setHorizontalHeaderLabels(["Name", "Number of dish"])

        self.Billing.clicked.connect(lambda: self.openBill())
        self.Billing.clicked.connect(lambda: menu.close())
        self.order.clicked.connect(lambda: self.openMessage())
        self.pushButton.clicked.connect(lambda: self.clear_order())
        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def add(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(button.pos())
        if index.isValid():
            name = self.tableWidget.item(index.row(), 0)
            number = self.tableWidget.item(index.row(), 2)
            if number is not None:
                if len(self.current_order) >= 2:
                    #     # self.tableOrder.setRowCount(len(order) + 1)
                    self.tableOrder.setRowCount(len(self.current_order) + 1)
                if name.text() not in self.current_order:
                    self.current_order[name.text()] = int(number.text())
                    item = QTableWidgetItem(name)
                    item2 = QTableWidgetItem(number.text())
                    self.tableOrder.setItem(self.order_row, 0, item)
                    self.tableOrder.setItem(self.order_row, 1, item2)
                    self.order_row += 1
                else:
                    self.current_order[name.text()] += int(number.text())
                    for i in range(self.tableOrder.rowCount()):
                        if self.tableOrder.item(i, 0).text() == name.text():
                            item2 = QTableWidgetItem(str(self.current_order[name.text()]))
                            self.tableOrder.setItem(i, 1, item2)
                            break

    def openMessage(self, ):
        self.tableOrder.clear()
        for key, value in self.current_order.items():
            if not self.order1.check(key):
                self.order1.add_to_order(key, value)
            else:
                self.order1.add_existed_to_order(key, value)

        self.order_row = 0
        self.current_order.clear()
        self.window = QtWidgets.QDialog()
        self.ui = message.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def openBill(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BillWindow(self.order1, self.menu_list)
        self.ui.setupUi(self.window)
        self.window.show()

    def clear_order(self):
        self.tableOrder.clear()
        self.order_row = 0
        self.current_order.clear()

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

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     menu = QtWidgets.QMainWindow()
#     ui = Ui_menu()
#     ui.setupUi(menu)
#     menu.show()
#     sys.exit(app.exec_())
