# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableModify.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from collections import OrderedDict
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_ModifyTable(object):
    def __init__(self):
        table_map = { }
        filePath = r"C:\Users\Asus\Documents\Restaurant\TableFile\TableDetail.txt"
        f = open(filePath, "r")
        for x in f:
            temp = x.split(":")
            table_map[int(temp[0])] = int(temp[1])
        f.close()
        self.tableDetail = dict(sorted(table_map.items(), key=lambda kv: kv[0]))

    def setupUi(self, ModifyTable):
        ModifyTable.setObjectName("ModifyTable")
        ModifyTable.resize(537, 640)
        self.centralwidget = QtWidgets.QWidget(ModifyTable)
        self.centralwidget.setObjectName("centralwidget")
        self.nameInput_del = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput_del.setGeometry(QtCore.QRect(370, 100, 111, 31))
        self.nameInput_del.setObjectName("nameInput_del")
        self.TableName_del = QtWidgets.QLineEdit(self.centralwidget)
        self.TableName_del.setEnabled(True)
        self.TableName_del.setGeometry(QtCore.QRect(370, 40, 111, 31))
        self.TableName_del.setObjectName("TableName_del")
        self.tableList = QtWidgets.QTableWidget(self.centralwidget)
        self.tableList.setGeometry(QtCore.QRect(20, 20, 291, 411))
        self.tableList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableList.setRowCount(5)
        self.tableList.setColumnCount(2)
        self.tableList.setObjectName("tableList")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(6)
        item.setFont(font)
        self.tableList.setItem(0, 3, item)
        self.tableList.horizontalHeader().setCascadingSectionResizes(True)
        self.tableList.horizontalHeader().setDefaultSectionSize(134)
        self.tableList.horizontalHeader().setStretchLastSection(False)
        self.tableList.verticalHeader().setCascadingSectionResizes(True)
        self.tableList.verticalHeader().setStretchLastSection(False)
        self.tableList.verticalHeader().hide()
        self.addTable = QtWidgets.QPushButton(self.centralwidget)
        self.addTable.setGeometry(QtCore.QRect(110, 600, 93, 28))
        self.addTable.setObjectName("addTable")
        self.deleteTable = QtWidgets.QPushButton(self.centralwidget)
        self.deleteTable.setGeometry(QtCore.QRect(380, 160, 93, 28))
        self.deleteTable.setObjectName("deleteTable")
        self.seatsInput = QtWidgets.QLineEdit(self.centralwidget)
        self.seatsInput.setGeometry(QtCore.QRect(200, 540, 61, 31))
        self.seatsInput.setObjectName("seatsInput")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(200, 480, 61, 31))
        self.nameInput.setObjectName("nameInput")
        self.SeatsText = QtWidgets.QLineEdit(self.centralwidget)
        self.SeatsText.setGeometry(QtCore.QRect(50, 540, 111, 31))
        self.SeatsText.setObjectName("SeatsText")
        self.TableName = QtWidgets.QLineEdit(self.centralwidget)
        self.TableName.setEnabled(True)
        self.TableName.setGeometry(QtCore.QRect(50, 480, 111, 31))
        self.TableName.setObjectName("TableName")
        ModifyTable.setCentralWidget(self.centralwidget)

        self.tableList.setHorizontalHeaderLabels(["Table number","Number of seats"])

        self.update_in_gui(self.tableDetail)

        self.addTable.clicked.connect(lambda: self.add_func())
        self.deleteTable.clicked.connect(lambda: self.del_func())

        self.retranslateUi(ModifyTable)
        QtCore.QMetaObject.connectSlotsByName(ModifyTable)

    def add_func(self):
        if self.nameInput.text() != None:
            new_table = int(self.nameInput.text())
            self.tableDetail[new_table] = int(self.seatsInput.text())
            self.tableDetail = dict(sorted(self.tableDetail.items(), key=lambda kv: kv[0]))
            self.update_in_file(self.tableDetail)
            self.update_in_gui(self.tableDetail)

    def del_func(self):
        if self.nameInput_del.text() != None:
            table_need_remove = int(self.nameInput_del.text())
            if table_need_remove in self.tableDetail:
                del self.tableDetail[table_need_remove]
                self.tableList.setRowCount(len(self.tableDetail) + 1)
                self.tableDetail = dict(sorted(self.tableDetail.items(), key=lambda kv: kv[0]))
                self.update_in_file(self.tableDetail)
                self.update_in_gui_after_del(self.tableDetail)

    def update_in_file(self,new_dict):
        filePath = r"C:\Users\Asus\Documents\Restaurant\TableFile\TableDetail.txt"
        f = open(filePath, "w")
        for key,value in new_dict.items():
            f.write(f"{key}:" +str(value)+"\n")
        f.close()

    def update_in_gui(self,new_dict):
        if len(new_dict) > 4:
            self.tableList.setRowCount(len(new_dict)+1)
        row = 0
        for key, value in new_dict.items():
            name_table = QTableWidgetItem(f"Table number {key}")
            number_of_seats = QTableWidgetItem(str(value))
            self.tableList.setItem(row, 0, name_table)
            self.tableList.setItem(row, 1, number_of_seats)
            row += 1

    def update_in_gui_after_del(self,new_dict):
        self.tableList.setRowCount(len(new_dict))
        row = 0
        for key, value in new_dict.items():
            name_table = QTableWidgetItem(f"Table number {key}")
            number_of_seats = QTableWidgetItem(str(value))
            self.tableList.setItem(row, 0, name_table)
            self.tableList.setItem(row, 1, number_of_seats)
            row += 1


    def retranslateUi(self, ModifyTable):
        _translate = QtCore.QCoreApplication.translate
        ModifyTable.setWindowTitle(_translate("ModifyTable", "ModifyTable"))
        self.TableName_del.setText(_translate("ModifyTable", "Table number"))
        __sortingEnabled = self.tableList.isSortingEnabled()
        self.tableList.setSortingEnabled(False)
        self.tableList.setSortingEnabled(__sortingEnabled)
        self.addTable.setText(_translate("ModifyTable", "Add Table"))
        self.deleteTable.setText(_translate("ModifyTable", "Delete Table"))
        self.SeatsText.setText(_translate("ModifyTable", "Number of seats"))
        self.TableName.setText(_translate("ModifyTable", "Table number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModifyTable = QtWidgets.QMainWindow()
    ui = Ui_ModifyTable()
    ui.setupUi(ModifyTable)
    ModifyTable.show()
    sys.exit(app.exec_())
