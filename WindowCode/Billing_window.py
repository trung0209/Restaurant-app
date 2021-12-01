import os
from qtpy import QtGui
import Started

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_BillWindow(object):  # billing
    def __init__(self, order1, menu_list):
        self.order1 = order1
        self.menu_list = menu_list

    def setupUi(self, BillWindow):
        BillWindow.setObjectName("BillWindow")
        BillWindow.resize(701, 616)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        BillWindow.setFont(font)
        BillWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(BillWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableBill = QtWidgets.QTableWidget(self.centralwidget)
        self.tableBill.setGeometry(QtCore.QRect(40, 20, 401, 531))
        self.tableBill.setRowCount(5)
        self.tableBill.setColumnCount(3)
        self.tableBill.setObjectName("tableBill")
        self.bill_id = QtWidgets.QLineEdit(self.centralwidget)
        self.bill_id.setGeometry(QtCore.QRect(552, 30, 141, 21))
        self.bill_id.setObjectName("bill_id")
        self.bill_name = QtWidgets.QLineEdit(self.centralwidget)
        self.bill_name.setGeometry(QtCore.QRect(460, 30, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bill_name.setFont(font)
        self.bill_name.setAlignment(QtCore.Qt.AlignCenter)
        self.bill_name.setReadOnly(True)
        self.bill_name.setObjectName("bill_name")
        self.Total_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Total_text.setGeometry(QtCore.QRect(460, 70, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Total_text.setFont(font)
        self.Total_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Total_text.setReadOnly(True)
        self.Total_text.setObjectName("Total_text")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(550, 70, 141, 31))
        self.total.setObjectName("total")
        self.finish = QtWidgets.QPushButton(self.centralwidget)
        self.finish.setGeometry(QtCore.QRect(530, 210, 81, 28))
        self.finish.setObjectName("finish")
        self.notice = QtWidgets.QLineEdit(self.centralwidget)
        self.notice.setGeometry(QtCore.QRect(510, 170, 121, 22))
        self.notice.setObjectName("notice")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(590, 530, 101, 28))
        self.back.setObjectName("back")
        self.feedBackBox = QtWidgets.QLineEdit(self.centralwidget)
        self.feedBackBox.setGeometry(QtCore.QRect(450, 250, 241, 211))
        self.feedBackBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.feedBackBox.setObjectName("feedBackBox")
        self.sumitFeedback = QtWidgets.QPushButton(self.centralwidget)
        self.sumitFeedback.setGeometry(QtCore.QRect(500, 470, 121, 28))
        self.sumitFeedback.setObjectName("sumitFeedback")
        self.TableText = QtWidgets.QLineEdit(self.centralwidget)
        self.TableText.setGeometry(QtCore.QRect(460, 120, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TableText.setFont(font)
        self.TableText.setAlignment(QtCore.Qt.AlignCenter)
        self.TableText.setReadOnly(True)
        self.TableText.setObjectName("TableText")
        self.tableInput = QtWidgets.QLineEdit(self.centralwidget)
        self.tableInput.setGeometry(QtCore.QRect(570, 120, 113, 31))
        self.tableInput.setObjectName("tableInput")
        BillWindow.setCentralWidget(self.centralwidget)

        if self.order1.get_lenght() <= 0:
            self.tableBill.setRowCount(5)
            self.tableBill.setColumnCount(3)
        else:
            self.tableBill.setRowCount(self.order1.get_lenght())
            self.tableBill.setColumnCount(3)

        total = 0
        row = 0  # Index of menu table bill
        temp = self.order1.get_dict().items()
        for key, value in temp:
            total += self.menu_list[key] * value
            if row > len(self.order1.get_dict()):
                break

            name = QTableWidgetItem(key)
            price = QTableWidgetItem(f"{str(self.menu_list[key])}₩")
            number = QTableWidgetItem(str(value))
            self.tableBill.setItem(row, 0, name)
            self.tableBill.setItem(row, 1, price)
            self.tableBill.setItem(row, 2, number)
            row += 1
        self.tableBill.setHorizontalHeaderLabels(["Name", "Price", "Number of dish"])
        self.bill_id.setText(str(self.order1.get_id()))
        self.total.setText(str(total)+"₩")
        self.sumitFeedback.clicked.connect(lambda: self.save_feed_back())
        self.finish.clicked.connect(lambda: self.sendNotice())
        self.back.clicked.connect(lambda: self.back_to_mainScreen())
        self.back.clicked.connect(lambda: BillWindow.close())
        self.retranslateUi(BillWindow)
        QtCore.QMetaObject.connectSlotsByName(BillWindow)

    def save_feed_back(self):
        save_path1 = r'FeedBack'
        file_name = f"Table number {self.tableInput.text()} {self.order1.get_id()}"

        completename1 = os.path.join(save_path1, file_name + ".txt")

        with open(completename1, 'w') as fp:
            fp.write(f"{self.feedBackBox.text()}")
        self.feedBackBox.setText("FeedBack Summited Thank You")

    def sendNotice(self):
        self.notice.setText("Complete!!!")
        save_path2 = r'RecordBill'
        file_name = f"Table number {self.tableInput.text()} {self.order1.get_id()}"

        completename2 = os.path.join(save_path2, file_name + ".txt")

        fo = open(completename2, "w")
        temp = self.order1.get_dict().items()
        for key, value in temp:
            prices = self.menu_list[key] * value
            fo.write(key + ":" + str(value) + ":" +str(prices) + "\n")
        fo.close()

    def back_to_mainScreen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Started.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, BillWindow):
        _translate = QtCore.QCoreApplication.translate
        BillWindow.setWindowTitle(_translate("BillWindow", "BillWindow"))
        self.bill_name.setText(_translate("BillWindow", "Bill Id:"))
        self.Total_text.setText(_translate("BillWindow", "Total:"))
        self.finish.setText(_translate("BillWindow", "Finish"))
        self.back.setText(_translate("BillWindow", "Back to Main"))
        self.sumitFeedback.setText(_translate("BillWindow", "Sumit Feedback"))
        self.TableText.setText(_translate("BillWindow", "Table Number"))
