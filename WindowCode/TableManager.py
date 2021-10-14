# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableManager.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton

from WindowCode import ManagerWindow


class Ui_TableManger(object):
    def __init__(self):
        table_map = {}
        filePath = r"C:\Users\Asus\Documents\Restaurant\TableFile\TableDetail.txt"
        f = open(filePath, "r")
        for x in f:
            temp = x.split(":")
            table_map[temp[0]] = int(temp[1])
        self.tableDetail = table_map


    def setupUi(self, TableManger):
        TableManger.setObjectName("TableManger")
        TableManger.resize(990, 656)
        self.centralwidget = QtWidgets.QWidget(TableManger)
        self.centralwidget.setObjectName("centralwidget")
        self.tableList = QtWidgets.QTableWidget(self.centralwidget)
        self.tableList.setGeometry(QtCore.QRect(10, 10, 961, 581))
        self.tableList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableList.setRowCount(5)
        self.tableList.setColumnCount(7)
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
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(840, 600, 111, 31))
        self.returnButton.setObjectName("returnButton")
        TableManger.setCentralWidget(self.centralwidget)

        self.tableList.setRowCount(len(self.tableDetail))
        self.tableList.setHorizontalHeaderLabels(["Table Number", "Number of seats", "Status", "Detail", "Check Button", "Uncheck Button", "Reservation"])

        row = 0
        for key, value in self.tableDetail.items():
            # print(f"{key}:{value}")
            name = "Number " + key
            table_name = QTableWidgetItem(name)

            number_seats = QTableWidgetItem(str(value))
            self.tableList.setItem(row, 0, table_name)
            self.tableList.setItem(row, 1, number_seats)

            self.check_btn = QPushButton('Check')
            self.uncheck_btn = QPushButton('UnCheck')
            self.reserve_btn = QPushButton('Reservation')
            self.tableList.setItem(row,2,QTableWidgetItem("Uncheck"))

            self.check_btn.clicked.connect(lambda: self.check())
            self.uncheck_btn.clicked.connect(lambda: self.un_check())
            self.reserve_btn.clicked.connect(lambda: self.reservation())

            self.tableList.setCellWidget(row, 4, self.check_btn)
            self.tableList.setCellWidget(row, 5, self.uncheck_btn)
            self.tableList.setCellWidget(row, 6, self.reserve_btn)
            row += 1

        self.returnButton.clicked.connect(lambda: self.exit())
        self.returnButton.clicked.connect(lambda: TableManger.close())
        self.retranslateUi(TableManger)
        QtCore.QMetaObject.connectSlotsByName(TableManger)

    def check(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableList.indexAt(button.pos())
        if index.isValid():
            status = self.tableList.item(index.row(),2)
            if status.text() != "Check":
                check_status = QTableWidgetItem("Check")
                self.tableList.setItem(index.row(),2,check_status)

    def un_check(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableList.indexAt(button.pos())
        if index.isValid():
            status = self.tableList.item(index.row(),2)
            if status.text() != "Uncheck":
                check_status = QTableWidgetItem("Uncheck")
                self.tableList.setItem(index.row(),2,check_status)

    def reservation(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableList.indexAt(button.pos())
        if index.isValid():
            status = self.tableList.item(index.row(),2)
            if status.text() != "Reservation" and status.text() == "Uncheck":
                check_status = QTableWidgetItem("Reservation")
                self.tableList.setItem(index.row(),2,check_status)
            elif status.text() == "Reservation":
                check_status = QTableWidgetItem("Uncheck")
                self.tableList.setItem(index.row(), 2, check_status)

    def exit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ManagerWindow.Ui_Manager()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, TableManger):
        _translate = QtCore.QCoreApplication.translate
        TableManger.setWindowTitle(_translate("TableManger", "TableManger"))
        __sortingEnabled = self.tableList.isSortingEnabled()
        self.tableList.setSortingEnabled(False)
        self.tableList.setSortingEnabled(__sortingEnabled)
        self.returnButton.setText(_translate("TableManger", "Back"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     TableManger = QtWidgets.QMainWindow()
#     ui = Ui_TableManger()
#     ui.setupUi(TableManger)
#     TableManger.show()
#     sys.exit(app.exec_())
