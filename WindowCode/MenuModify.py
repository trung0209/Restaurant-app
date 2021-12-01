# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuModify.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_MenuModify(object):
    def __init__(self):
        self.dish_map = { }
        filePath = r"Menu\Menu.txt"
        f = open(filePath, "r")
        for x in f:
            temp = x.split(":")
            self.dish_map[temp[0]] = int(temp[1])
        f.close()

    def setupUi(self, MenuModify):
        MenuModify.setObjectName("MenuModify")
        MenuModify.resize(662, 562)
        self.centralwidget = QtWidgets.QWidget(MenuModify)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 371, 511))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget.verticalHeader().hide()
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(410, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.name_dish = QtWidgets.QLineEdit(self.centralwidget)
        self.name_dish.setGeometry(QtCore.QRect(510, 30, 121, 31))
        self.name_dish.setObjectName("name_dish")
        self.priceEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.priceEdit.setGeometry(QtCore.QRect(510, 80, 121, 31))
        self.priceEdit.setObjectName("priceEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(410, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.name_dish_del = QtWidgets.QLineEdit(self.centralwidget)
        self.name_dish_del.setGeometry(QtCore.QRect(520, 190, 121, 31))
        self.name_dish_del.setObjectName("name_dish_del")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 250, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MenuModify.setCentralWidget(self.centralwidget)

        self.update_in_gui(self.dish_map)
        self.pushButton.clicked.connect(lambda: self.add_func())
        self.pushButton_2.clicked.connect(lambda: self.del_func())

        self.retranslateUi(MenuModify)
        QtCore.QMetaObject.connectSlotsByName(MenuModify)

    def update_in_gui(self,new_dict):
        if len(new_dict) > 4:
            self.tableWidget.setRowCount(len(new_dict)+1)
        row = 0
        for key, value in new_dict.items():
            dish_name = QTableWidgetItem(f"{key}")
            price = QTableWidgetItem(str(value)+"₩")
            self.tableWidget.setItem(row, 0, dish_name)
            self.tableWidget.setItem(row, 1, price)
            row += 1

    def update_in_gui_after_del(self,new_dict):
        self.tableWidget.setRowCount(len(new_dict))
        row = 0
        for key, value in new_dict.items():
            dish_name = QTableWidgetItem(f"{key}")
            price = QTableWidgetItem(str(value) + "₩")
            self.tableWidget.setItem(row, 0, dish_name)
            self.tableWidget.setItem(row, 1, price)
            row += 1

    def update_in_file(self,new_dict):
        file_path = r"Menu\Menu.txt"
        f = open(file_path, "w")
        for key,value in new_dict.items():
            f.write(f"{key}:" +str(value)+"\n")
        f.close()

    def add_func(self):
        if self.name_dish.text() is not None:
            new_dish = self.name_dish.text().capitalize()
            self.dish_map[new_dish] = int(self.priceEdit.text())
            self.update_in_file(self.dish_map)
            self.update_in_gui(self.dish_map)

    def del_func(self):
        if self.name_dish_del.text() is not None:
            dish_need_remove = self.name_dish_del.text().capitalize()
            if dish_need_remove in self.dish_map:
                del self.dish_map[dish_need_remove]
                self.tableWidget.setRowCount(len(self.dish_map) + 1)
                self.update_in_file(self.dish_map)
                self.update_in_gui_after_del(self.dish_map)

    def retranslateUi(self, MenuModify):
        _translate = QtCore.QCoreApplication.translate
        MenuModify.setWindowTitle(_translate("MenuModify", "MenuModify"))
        self.lineEdit.setText(_translate("MenuModify", "Dish name:"))
        self.lineEdit_2.setText(_translate("MenuModify", "Price:"))
        self.pushButton.setText(_translate("MenuModify", "Add Dish"))
        self.lineEdit_3.setText(_translate("MenuModify", "Dish name:"))
        self.pushButton_2.setText(_translate("MenuModify", "Delete Dish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuModify = QtWidgets.QMainWindow()
    ui = Ui_MenuModify()
    ui.setupUi(MenuModify)
    MenuModify.show()
    sys.exit(app.exec_())
