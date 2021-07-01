# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyTable.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
from dbfread import DBF
from PyQt5.QtCore import QRegExp, QDate, QTime, QDateTime, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QCompleter
import dbf
import datetime
from time import strftime
import inspect
import sqlite3
import os


now = datetime.datetime.now()


class Ui_MainWindow(object):
    def __init__(self):
        if os.path.exists('dbLocation.txt'):
            with open("dbLocation.txt", "r")as dbLocation:
                self.dbLocal = dbLocation.read()
        else:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.dbLocal, _ = QFileDialog.getOpenFileName(MainWindow, "Select the belco911.sqlite file ", "",
                                                          "All Files (*);;Database Files (*.db)", options=options)
            with open("dbLocation.txt", "w")as newDbLocation:
                newDbLocation.write(self.dbLocal)
        self.TypesOfStreets = []
        self.rdNameList = []
        self.communityList = []
        self.esnList = []
        self.searchList = []
        self.mapNumList = []
        self.streetName = []
        self.streetList = []
        self.conn = sqlite3.connect(self.dbLocal)
        self.c = self.conn.cursor()
        self.now = QDate.currentDate()


    def loadData(self):
        self.c.execute('SELECT * FROM housenum WHERE map_no > 0 AND township = "RICHLAND" ORDER BY map_no ASC')
        self.editTable = self.c.fetchall()
        with self.conn:
            self.tableWidget.setSortingEnabled(False)
            self.tableWidget.setRowCount(0)
            self.c.execute('SELECT DISTINCT trim(st_type) FROM housenum')
            self.TypesOfStreets = self.c.fetchall()
            self.c.execute('SELECT DISTINCT trim(community) FROM housenum')
            self.communityList = self.c.fetchall()
            self.c.execute('SELECT DISTINCT trim(esn) FROM housenum')
            self.esnList = self.c.fetchall()
            self.c.execute('SELECT DISTINCT trim(map_no) FROM housenum WHERE map_no > 0')
            self.mapNumList = self.c.fetchall()
            self.c.execute('SELECT DISTINCT trim(st_name) FROM housenum')
            self.streetName = self.c.fetchall()
            self.streetList = [x[0] for x in self.streetName]
            streetCompleter = QCompleter(self.streetList)
            self.txtStreetName.setCompleter(streetCompleter)

            for row_number, row_data in enumerate(self.editTable):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.tableWidget.setSortingEnabled(True)

    def loadSearch(self, searchTable):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(searchTable):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1387, 898)
        MainWindow.setFixedSize(1300, 898)
        MainWindow.setWindowIcon(QtGui.QIcon("seal.ico"))
        labelFont = QtGui.QFont()
        labelFont.setPointSize(8)
        labelFont.setBold(True)
        labelFont.setWeight(50)
        labelFont.setFamily("Arial")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 480, 1281, 391))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(30)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(29, item)
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setColumnHidden(1, True)
        self.tableWidget.setColumnHidden(5, True)
        self.tableWidget.setColumnHidden(20, True)
        self.tableWidget.setColumnHidden(21, True)
        self.tableWidget.setColumnHidden(22, True)
        self.tableWidget.setColumnHidden(9, True)
        self.tableWidget.setColumnHidden(12, False)
        self.tableWidget.setColumnHidden(15, False)
        self.tableWidget.setColumnHidden(16, False)
        self.tableWidget.setColumnHidden(23, True)
        self.tableWidget.setColumnHidden(24, True)
        self.tableWidget.setColumnHidden(25, True)
        # self.tableWidget.setColumnHidden(26, True)
        self.tableWidget.setColumnHidden(27, True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 631, 377))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setFont(labelFont)
        self.txtHnID = QtWidgets.QLineEdit(self.groupBox)
        self.txtHnID.setGeometry(QtCore.QRect(10, 40, 541, 20))
        self.txtHnID.setText("")
        self.txtHnID.setReadOnly(True)
        self.txtHnID.setObjectName("txtHnID")

        self.cmbMapNum = QtWidgets.QComboBox(self.groupBox)
        self.cmbMapNum.setGeometry(QtCore.QRect(560, 40, 66, 20))
        self.cmbMapNum.setEditable(True)
        self.cmbMapNum.setObjectName("cmbMapNum")
        self.cmbMapNum.addItem("")
        self.cmbMapNum.setItemText(0, "")
        self.cmbMapNum.addItem("")
        reg_ex = QRegExp("[0-9]\\d{0,5}")
        mapNum_validator = QRegExpValidator(reg_ex, self.cmbMapNum)
        self.cmbMapNum.setValidator(mapNum_validator)
        toComplete = []
        c = QCompleter(toComplete)
        self.cmbMapNum.setCompleter(c)
        self.txtHN = QtWidgets.QLineEdit(self.groupBox)
        self.txtHN.setGeometry(QtCore.QRect(10, 90, 61, 20))
        self.txtHN.setObjectName("txtHN")
        self.txtHN.setReadOnly(False)
        # self.txtHN.textChanged.connect(self.toUpper)
        self.txtHN_suffix = QtWidgets.QLineEdit(self.groupBox)
        self.txtHN_suffix.setGeometry(QtCore.QRect(80, 90, 61, 20))
        self.txtHN_suffix.setObjectName("txtHN_suffix")
        self.txtHN_suffix.setReadOnly(False)
        self.txtHN_suffix.textChanged.connect(lambda: self.to_upper(self.txtHN_suffix))
        # self.txtHN_suffix.textChanged.connect(self.toUpper)
        self.txtPreDir = QtWidgets.QLineEdit(self.groupBox)
        self.txtPreDir.setGeometry(QtCore.QRect(160, 90, 61, 20))
        self.txtPreDir.setObjectName("txtPreDir")
        self.txtPreDir.setReadOnly(False)
        self.txtPreDir.textChanged.connect(lambda: self.to_upper(self.txtPreDir))
        # self.txtPreDir.textChanged.connect(self.toUpper)
        self.txtStreetName = QtWidgets.QLineEdit(self.groupBox)
        self.txtStreetName.setGeometry(QtCore.QRect(230, 90, 251, 20))
        self.txtStreetName.setObjectName("txtStreetName")
        self.txtStreetName.setReadOnly(False)

        self.txtStreetName.textChanged.connect(lambda: self.to_upper(self.txtStreetName))
        self.txtStreetName.textChanged.connect(lambda: self.streetCheck(self.txtStreetName.text()))
        self.txtStreetName.editingFinished.connect(lambda: self.streetCheck(self.txtStreetName.text()))

        self.cmbStType = QtWidgets.QComboBox(self.groupBox)
        self.cmbStType.setGeometry(QtCore.QRect(490, 90, 61, 22))
        self.cmbStType.setEditable(True)
        self.cmbStType.setObjectName("cmbStType")
        self.cmbStType.addItem("")
        self.cmbStType.setItemText(0, "")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.addItem("")
        self.cmbStType.editTextChanged.connect(self.AddyCheck)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(15, 20, 120, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(15, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 70, 71, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(160, 70, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(230, 70, 80, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(490, 70, 69, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(565, 70, 57, 16))
        self.label_7.setObjectName("label_7")
        self.txtStreetDir = QtWidgets.QLineEdit(self.groupBox)
        self.txtStreetDir.setGeometry(QtCore.QRect(560, 90, 61, 20))
        self.txtStreetDir.setObjectName("txtStreetDir")
        self.txtStreetDir.setReadOnly(False)
        self.txtStreetDir.textChanged.connect(lambda: self.to_upper(self.txtStreetDir))
        self.txtStreetDir.editingFinished.connect(self.AddyCheck)
        # self.txtStreetDir.textChanged.connect(self.toUpper)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(565, 20, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(15, 120, 70, 16))
        self.label_9.setObjectName("label_9")
        self.txtLastName = QtWidgets.QLineEdit(self.groupBox)
        self.txtLastName.setGeometry(QtCore.QRect(10, 140, 291, 20))
        self.txtLastName.setObjectName("txtLastName")
        self.txtLastName.setReadOnly(False)
        self.txtLastName.textChanged.connect(lambda: self.to_upper(self.txtLastName))
        # self.txtLastName.textChanged.connect(self.toUpper)
        self.txtFirstName = QtWidgets.QLineEdit(self.groupBox)
        self.txtFirstName.setGeometry(QtCore.QRect(330, 140, 291, 20))
        self.txtFirstName.setObjectName("txtFirstName")
        self.txtFirstName.setReadOnly(False)
        self.txtFirstName.textChanged.connect(lambda: self.to_upper(self.txtFirstName))
        # self.txtFirstName.textChanged.connect(self.toUpper)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(335, 120, 70, 16))
        self.label_10.setObjectName("label_10")
        self.txtLastName_2 = QtWidgets.QLineEdit(self.groupBox)
        self.txtLastName_2.setGeometry(QtCore.QRect(10, 190, 291, 20))
        self.txtLastName_2.setObjectName("txtLastName_2")
        self.txtLastName_2.setReadOnly(False)
        self.txtLastName_2.textChanged.connect(lambda: self.to_upper(self.txtLastName_2))
        # self.txtLastName_2.textChanged.connect(self.toUpper)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(15, 170, 61, 16))
        self.label_11.setObjectName("label_11")
        self.cmbCity = QtWidgets.QComboBox(self.groupBox)
        self.cmbCity.setGeometry(QtCore.QRect(310, 190, 151, 22))
        self.cmbCity.setEditable(True)
        self.cmbCity.setObjectName("cmbCity")
        self.cmbCity.setItemText(0, "")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.cmbCity.addItem("")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(310, 170, 31, 16))
        self.label_12.setObjectName("label_12")
        self.cmbMailCity = QtWidgets.QComboBox(self.groupBox)
        self.cmbMailCity.setGeometry(QtCore.QRect(470, 190, 151, 22))
        self.cmbMailCity.setEditable(True)
        self.cmbMailCity.setObjectName("cmbMailCity")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.setItemText(0, "")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")
        self.cmbMailCity.addItem("")

        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(480, 170, 50, 16))
        self.label_13.setObjectName("label_13")
        self.cmbComm = QtWidgets.QComboBox(self.groupBox)
        self.cmbComm.setGeometry(QtCore.QRect(10, 240, 151, 22))
        self.cmbComm.setEditable(True)
        self.cmbComm.setObjectName("cmbComm")
        self.cmbComm.addItem("")
        self.cmbComm.setItemText(0, "")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(15, 220, 70, 16))
        self.label_14.setObjectName("label_14")
        self.txtSubdiv = QtWidgets.QLineEdit(self.groupBox)
        self.txtSubdiv.setGeometry(QtCore.QRect(170, 240, 221, 20))
        self.txtSubdiv.setObjectName("txtSubdiv")
        self.txtSubdiv.setReadOnly(False)
        self.txtSubdiv.textChanged.connect(lambda: self.to_upper(self.txtSubdiv))
        # self.txtSubdiv.textChanged.connect(self.toUpper)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(175, 220, 70, 16))
        self.label_15.setObjectName("label_15")
        self.txtBusinessName = QtWidgets.QLineEdit(self.groupBox)
        self.txtBusinessName.setGeometry(QtCore.QRect(400, 240, 221, 20))
        self.txtBusinessName.setObjectName("txtBusinessName")
        self.txtBusinessName.setReadOnly(False)
        self.txtBusinessName.textChanged.connect(lambda: self.to_upper(self.txtBusinessName))
        # self.txtBusinessName.textChanged.connect(self.toUpper)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(400, 220, 100, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(15, 270, 61, 16))
        self.label_17.setObjectName("label_17")
        self.cmbTownship = QtWidgets.QComboBox(self.groupBox)
        self.cmbTownship.setGeometry(QtCore.QRect(10, 290, 151, 22))
        self.cmbTownship.setEditable(True)
        self.cmbTownship.setObjectName("cmbTownship")
        self.cmbTownship.addItem("")
        self.cmbTownship.setItemText(0, "")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")
        self.cmbTownship.addItem("")

        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(175, 270, 47, 13))
        self.label_18.setObjectName("label_18")
        self.txtRdNum = QtWidgets.QLineEdit(self.groupBox)
        self.txtRdNum.setGeometry(QtCore.QRect(170, 290, 61, 20))
        self.txtRdNum.setObjectName("txtRdNum")
        self.txtRdNum.setReadOnly(False)
        self.txtRdNum.textChanged.connect(lambda: self.to_upper(self.txtRdNum))
        # self.txtRdNum.textChanged.connect(self.toUpper)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(240, 290, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setReadOnly(False)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(245, 270, 80, 16))
        self.label_19.setObjectName("label_19")
        self.cmbESN = QtWidgets.QComboBox(self.groupBox)
        self.cmbESN.setGeometry(QtCore.QRect(10, 340, 61, 22))
        self.cmbESN.setEditable(True)
        self.cmbESN.setObjectName("cmbESN")
        self.cmbESN.addItem("")
        self.cmbESN.setItemText(0, "")
        self.cmbESN.currentIndexChanged.connect(self.esnUpdate)

        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(10, 320, 61, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(90, 320, 31, 16))
        self.label_21.setObjectName("label_21")
        self.txtFire = QtWidgets.QLineEdit(self.groupBox)
        self.txtFire.setGeometry(QtCore.QRect(90, 340, 171, 20))
        self.txtFire.setObjectName("txtFire")
        self.txtFire.setReadOnly(False)
        self.txtFire.textChanged.connect(lambda: self.to_upper(self.txtFire))
        # self.txtFire.textChanged.connect(self.toUpper)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(270, 320, 50, 16))
        self.label_22.setObjectName("label_22")
        self.txtPolice = QtWidgets.QLineEdit(self.groupBox)
        self.txtPolice.setGeometry(QtCore.QRect(270, 340, 171, 20))
        self.txtPolice.setObjectName("txtPolice")
        self.txtPolice.setReadOnly(False)
        self.txtPolice.textChanged.connect(lambda: self.to_upper(self.txtPolice))
        # self.txtPolice.textChanged.connect(self.toUpper)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(450, 320, 50, 16))
        self.label_23.setObjectName("label_23")
        self.txtEMS = QtWidgets.QLineEdit(self.groupBox)
        self.txtEMS.setGeometry(QtCore.QRect(450, 340, 171, 20))
        self.txtEMS.setObjectName("txtEMS")
        self.txtEMS.setReadOnly(False)
        self.txtEMS.textChanged.connect(lambda: self.to_upper(self.txtEMS))

        self.btnInsert = QtWidgets.QPushButton(self.groupBox)
        self.btnInsert.setGeometry(QtCore.QRect(450, 270, 75, 23))
        self.btnInsert.setObjectName("btnInsert")
        self.btnInsert.setFont(labelFont)
        self.btnInsert.clicked.connect(self.insertIt_on_click)

        self.btnDel = QtWidgets.QPushButton(self.groupBox)
        self.btnDel.setGeometry(QtCore.QRect(530, 270, 75, 23))
        self.btnDel.setToolTip('Click here to delete current record')
        self.btnDel.setObjectName("btnDel")
        self.btnDel.setFont(labelFont)
        self.btnDel.clicked.connect(self.deleteIt_on_click)

        self.btnMapIt = QtWidgets.QPushButton(self.groupBox)
        self.btnMapIt.setGeometry(QtCore.QRect(530, 295, 75, 23))
        self.btnMapIt.setToolTip('Click here to zoom to this address in ArcMap')
        self.btnMapIt.setObjectName("btnMapIt")
        self.btnMapIt.setFont(labelFont)
        self.btnMapIt.clicked.connect(self.mapIt_on_click)

        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(0, 10, 1300, 61))
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setStyleSheet("QLabel {background-color: red;} QLabel#label_24 {color: black}")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_24.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_24.setFont(font)
        self.label_24.setAcceptDrops(False)
        self.label_24.setAutoFillBackground(False)
        self.label_24.setObjectName("label_24")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1030, 80, 261, 331))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setFont(labelFont)

        self.txtLastNameSearch = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtLastNameSearch.setGeometry(QtCore.QRect(10, 40, 231, 31))
        self.txtLastNameSearch.setObjectName("txtLastNameSearch")
        self.txtLastNameSearch.textChanged.connect(lambda: self.dbSearch(self.txtLastNameSearch, "lname"))

        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(20, 20, 70, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(20, 80, 90, 16))
        self.label_27.setObjectName("label_27")
        self.txtHouseNumSearch_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtHouseNumSearch_2.setGeometry(QtCore.QRect(10, 100, 231, 31))
        self.txtHouseNumSearch_2.setObjectName("txtHouseNumSearch_2")

        input_validator = QRegExpValidator(reg_ex, self.txtHouseNumSearch_2)
        self.txtHouseNumSearch_2.setValidator(input_validator)
        self.txtHouseNumSearch_2.textChanged.connect(lambda: self.dbSearch(self.txtHouseNumSearch_2, "housenum"))

        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(20, 140, 80, 16))
        self.label_28.setObjectName("label_28")

        self.txtRdNumSearch = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtRdNumSearch.setGeometry(QtCore.QRect(10, 160, 231, 31))
        self.txtRdNumSearch.setObjectName("txtRdNumSearch")
        self.txtRdNumSearch.textChanged.connect(lambda: self.dbSearch(self.txtRdNumSearch, "road_no"))

        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(20, 200, 70, 16))
        self.label_29.setObjectName("label_29")

        self.txtRdNameSearch = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtRdNameSearch.setGeometry(QtCore.QRect(10, 220, 231, 31))
        self.txtRdNameSearch.setObjectName("txtRdNameSearch")
        self.txtRdNameSearch.textChanged.connect(lambda: self.dbSearch(self.txtRdNameSearch, "st_name"))

        self.lblMapNumSearch = QtWidgets.QLabel(self.groupBox_2)
        self.lblMapNumSearch.setGeometry(QtCore.QRect(20, 260, 80, 16))
        self.lblMapNumSearch.setObjectName("lblMapNumSearch")

        self.txtMapNumSearch = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtMapNumSearch.setGeometry(QtCore.QRect(10, 280, 231, 31))
        self.txtMapNumSearch.setObjectName("txtMapNumSearch")
        self.txtMapNumSearch.textChanged.connect(lambda: self.dbSearch(self.txtMapNumSearch, "map_no"))

        self.btnClearSearch = QtWidgets.QPushButton(self.groupBox)
        self.btnClearSearch.setGeometry(QtCore.QRect(370, 295, 75, 23))
        self.btnClearSearch.setToolTip('Click to clear search text boxes')
        self.btnClearSearch.setObjectName("btnClearSearch")
        self.btnClearSearch.setFont(labelFont)
        self.btnClearSearch.clicked.connect(self.clrFields)



        self.btnNewRecord = QtWidgets.QPushButton(self.groupBox)
        self.btnNewRecord.setGeometry(QtCore.QRect(370, 270, 75, 23))
        self.btnNewRecord.setToolTip('Click to clear search text boxes for a new record')
        self.btnNewRecord.setObjectName("btnNewRecord")
        self.btnNewRecord.setFont(labelFont)
        self.btnNewRecord.clicked.connect(self.newRecord)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1030, 410, 261, 47))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setFont(labelFont)

        self.btnZeroMapNumReport = QtWidgets.QPushButton(self.groupBox_3)
        self.btnZeroMapNumReport.setGeometry(QtCore.QRect(10, 17, 75, 23))
        self.btnZeroMapNumReport.setObjectName("btnZeroMapNumReport")
        self.btnZeroMapNumReport.setFont(labelFont)
        self.btnZeroMapNumReport.clicked.connect(self.zeroMapNumReport)

        self.btnDupMapNumReport = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDupMapNumReport.setGeometry(QtCore.QRect(90, 17, 75, 23))
        self.btnDupMapNumReport.setObjectName("btnDupMapNumReport")
        self.btnDupMapNumReport.setFont(labelFont)
        self.btnDupMapNumReport.clicked.connect(self.dupMapReport)

        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(170, 17, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(labelFont)
        self.pushButton.clicked.connect(self.closeApp)

        self.grpOwnerData = QtWidgets.QGroupBox(self.centralwidget)
        self.grpOwnerData.setGeometry(QtCore.QRect(650, 80, 371, 377))
        self.grpOwnerData.setObjectName("grpOwnerData")
        self.grpOwnerData.setFont(labelFont)

        self.txtLastNameEngnr = QtWidgets.QLineEdit(self.grpOwnerData)
        self.txtLastNameEngnr.setGeometry(QtCore.QRect(10, 40, 231, 31))
        self.txtLastNameEngnr.setObjectName("txtLastNameEngnr")
        self.txtLastNameEngnr.setReadOnly(True)

        self.chkExclude = QtWidgets.QCheckBox(self.grpOwnerData)
        self.chkExclude.setGeometry(QtCore.QRect(10, 300, 121, 20))
        self.chkExclude.setObjectName("chkExclude")

        self.lblEngineers_lname = QtWidgets.QLabel(self.grpOwnerData)
        self.lblEngineers_lname.setGeometry(QtCore.QRect(20, 20, 250, 16))
        self.lblEngineers_lname.setObjectName("lblEngineers_lname")
        self.lblEngineers_fname = QtWidgets.QLabel(self.grpOwnerData)
        self.lblEngineers_fname.setGeometry(QtCore.QRect(20, 80, 250, 16))
        self.lblEngineers_fname.setObjectName("lblEngineers_fname")
        self.txtFirstNameEngnr = QtWidgets.QLineEdit(self.grpOwnerData)
        self.txtFirstNameEngnr.setGeometry(QtCore.QRect(10, 100, 231, 31))
        self.txtFirstNameEngnr.setObjectName("txtFirstNameEngnr")
        self.txtFirstNameEngnr.setReadOnly(True)
        self.txtNameAuditor = QtWidgets.QLineEdit(self.grpOwnerData)
        self.txtNameAuditor.setGeometry(QtCore.QRect(10, 160, 341, 31))
        self.txtNameAuditor.setObjectName("txtNameAuditor")
        self.txtNameAuditor.setReadOnly(True)
        self.lblAuditors_name = QtWidgets.QLabel(self.grpOwnerData)
        self.lblAuditors_name.setGeometry(QtCore.QRect(20, 140, 250, 16))
        self.lblAuditors_name.setObjectName("lblAuditors_name")
        self.txtParcelPin = QtWidgets.QLineEdit(self.grpOwnerData)
        self.txtParcelPin.setGeometry(QtCore.QRect(10, 220, 231, 31))
        self.txtParcelPin.setObjectName("txtParcelPin")
        self.txtParcelPin.setReadOnly(True)
        self.lblEngineers_fname_2 = QtWidgets.QLabel(self.grpOwnerData)
        self.lblEngineers_fname_2.setGeometry(QtCore.QRect(20, 200, 70, 16))
        self.lblEngineers_fname_2.setObjectName("lblEngineers_fname_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)

        self.loadData()
        self.loadMapList()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Belmont County 911"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HN_ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "HOUSE #"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "HOUSE # SUFFIX"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "PRE DIR"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PRE TYPE"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "STREET NAME"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "STREET TYPE"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "SUFFIX DIR"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "ADDRESS 2"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "CITY"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "FIRST NAME"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "LAST NAME"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "MAIL CITY"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "TOWNSHIP"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "ROAD #"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "MAP #"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "ESN"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "BUSINESS NAME"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "COMMUNITY"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "SUBDIVISION"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "ROAD NAME"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "DIRECTION"))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "PHONE"))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "FIRE"))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "POLICE"))
        item = self.tableWidget.horizontalHeaderItem(26)
        item.setText(_translate("MainWindow", "EMS"))
        item = self.tableWidget.horizontalHeaderItem(27)
        item.setText(_translate("MainWindow", "DATE UPDATED"))
        item = self.tableWidget.horizontalHeaderItem(28)
        item.setText(_translate("MainWindow", "JURISDICTION"))
        item = self.tableWidget.horizontalHeaderItem(29)
        item.setText(_translate("MainWindow", "EXCLUDE"))
        self.groupBox.setTitle(_translate("MainWindow", "House Numbering Database Addressing Info"))
        self.cmbMapNum.setItemText(1, _translate("MainWindow", ""))
        self.cmbStType.setItemText(1, _translate("MainWindow", "ALY"))
        self.cmbStType.setItemText(2, _translate("MainWindow", "AVE"))
        self.cmbStType.setItemText(2, _translate("MainWindow", "AV"))
        self.cmbStType.setItemText(3, _translate("MainWindow", "BLVD"))
        self.cmbStType.setItemText(4, _translate("MainWindow", "CIR"))
        self.cmbStType.setItemText(5, _translate("MainWindow", "CT"))
        self.cmbStType.setItemText(6, _translate("MainWindow", "DR"))
        self.cmbStType.setItemText(7, _translate("MainWindow", "EXT"))
        self.cmbStType.setItemText(8, _translate("MainWindow", "HTS"))
        self.cmbStType.setItemText(9, _translate("MainWindow", "HWY"))
        self.cmbStType.setItemText(10, _translate("MainWindow", "LN"))
        self.cmbStType.setItemText(11, _translate("MainWindow", "MEA"))
        self.cmbStType.setItemText(12, _translate("MainWindow", "PIKE"))
        self.cmbStType.setItemText(13, _translate("MainWindow", "PKWY"))
        self.cmbStType.setItemText(14, _translate("MainWindow", "RD"))
        self.cmbStType.setItemText(15, _translate("MainWindow", "RDG"))
        self.cmbStType.setItemText(16, _translate("MainWindow", "ROW"))
        self.cmbStType.setItemText(17, _translate("MainWindow", "ST"))
        self.cmbStType.setItemText(18, _translate("MainWindow", "TRL"))
        self.cmbStType.setItemText(19, _translate("MainWindow", "WAY"))
        self.label.setText(_translate("MainWindow", "House Number ID"))
        self.label_2.setText(_translate("MainWindow", "House #"))
        self.label_3.setText(_translate("MainWindow", "House # Suff"))
        self.label_4.setText(_translate("MainWindow", "Pre Dir"))
        self.label_5.setText(_translate("MainWindow", "Street Name"))
        self.label_6.setText(_translate("MainWindow", "Street Type"))
        self.label_7.setText(_translate("MainWindow", "Street Dir"))
        self.label_8.setText(_translate("MainWindow", "Map #"))
        self.label_9.setText(_translate("MainWindow", "Last Name"))
        self.label_10.setText(_translate("MainWindow", "First Name"))
        self.label_11.setText(_translate("MainWindow", "Address 2"))
        self.cmbCity.setItemText(1, _translate("MainWindow", "ARMSTRONG MILLS"))
        self.cmbCity.setItemText(2, _translate("MainWindow", "AVONDALE"))
        self.cmbCity.setItemText(3, _translate("MainWindow", "BAILEYS MILLS"))
        self.cmbCity.setItemText(4, _translate("MainWindow", "BANNOCK"))
        self.cmbCity.setItemText(5, _translate("MainWindow", "BARTON"))
        self.cmbCity.setItemText(6, _translate("MainWindow", "BEL HAVEN"))
        self.cmbCity.setItemText(7, _translate("MainWindow", "BELLAIRE"))
        self.cmbCity.setItemText(8, _translate("MainWindow", "BELLE VILLAGE"))
        self.cmbCity.setItemText(9, _translate("MainWindow", "BELLVIEW HEIGHTS"))
        self.cmbCity.setItemText(10, _translate("MainWindow", "BAINE"))
        self.cmbCity.setItemText(11, _translate("MainWindow", "BAINESVILLE"))
        self.cmbCity.setItemText(12, _translate("MainWindow", "BLOOMINGDALE"))
        self.cmbCity.setItemText(13, _translate("MainWindow", "BONAR ALLOT"))
        self.cmbCity.setItemText(14, _translate("MainWindow", "BOSTON"))
        self.cmbCity.setItemText(15, _translate("MainWindow", "BOYDSVILLE"))
        self.cmbCity.setItemText(16, _translate("MainWindow", "BRIDGEPORT"))
        self.cmbCity.setItemText(17, _translate("MainWindow", "BROOKFIELD"))
        self.cmbCity.setItemText(18, _translate("MainWindow", "BROOKVIEW TERRACE"))
        self.cmbCity.setItemText(19, _translate("MainWindow", "BROOKVIEW TR CT"))
        self.cmbCity.setItemText(20, _translate("MainWindow", "BRUESVILLE"))
        self.cmbCity.setItemText(21, _translate("MainWindow", "CANTERBURY ESTATE"))
        self.cmbCity.setItemText(22, _translate("MainWindow", "CAPTORS ADDITION"))
        self.cmbCity.setItemText(23, _translate("MainWindow", "CASA-HIJA SUB"))
        self.cmbCity.setItemText(24, _translate("MainWindow", "CENTERVILLE"))
        self.cmbCity.setItemText(25, _translate("MainWindow", "CHERRY FORREST"))
        self.cmbCity.setItemText(26, _translate("MainWindow", "CLARKSBURG"))
        self.cmbCity.setItemText(27, _translate("MainWindow", "COLERAIN"))
        self.cmbCity.setItemText(28, _translate("MainWindow", "CONSERVANCY"))
        self.cmbCity.setItemText(29, _translate("MainWindow", "COUNTRY COURT"))
        self.cmbCity.setItemText(30, _translate("MainWindow", "CRESCENT"))
        self.cmbCity.setItemText(31, _translate("MainWindow", "CRESTVIEW ESTATE"))
        self.cmbCity.setItemText(32, _translate("MainWindow", "CTRY CLUB EST"))
        self.cmbCity.setItemText(33, _translate("MainWindow", "DIX ADDITION"))
        self.cmbCity.setItemText(34, _translate("MainWindow", "DUDEKS ADD"))
        self.cmbCity.setItemText(35, _translate("MainWindow", "EAST LORETTO"))
        self.cmbCity.setItemText(36, _translate("MainWindow", "EAST RICHLAND"))
        self.cmbCity.setItemText(37, _translate("MainWindow", "ECHO"))
        self.cmbCity.setItemText(38, _translate("MainWindow", "EDGEWATER PARK"))
        self.cmbCity.setItemText(39, _translate("MainWindow", "EVICKS 1ST SUB"))
        self.cmbCity.setItemText(40, _translate("MainWindow", "EVICKS SUB-DIV"))
        self.cmbCity.setItemText(41, _translate("MainWindow", "FAIRPOINT"))
        self.cmbCity.setItemText(42, _translate("MainWindow", "FERRYVIEW"))
        self.cmbCity.setItemText(43, _translate("MainWindow", "FLORENCE"))
        self.cmbCity.setItemText(44, _translate("MainWindow", "FLUSHING"))
        self.cmbCity.setItemText(45, _translate("MainWindow", "FOREST GLEN"))
        self.cmbCity.setItemText(46, _translate("MainWindow", "FORNTIERSMANS VIEW"))
        self.cmbCity.setItemText(47, _translate("MainWindow", "FOX-SHANNON PLACE"))
        self.cmbCity.setItemText(48, _translate("MainWindow", "GIBBAS SUB"))
        self.cmbCity.setItemText(49, _translate("MainWindow", "GIFFEN ADDITION"))
        self.cmbCity.setItemText(50, _translate("MainWindow", "GIFFIN ADDITION"))
        self.cmbCity.setItemText(51, _translate("MainWindow", "GLENCO"))
        self.cmbCity.setItemText(52, _translate("MainWindow", "GLENEYRE"))
        self.cmbCity.setItemText(53, _translate("MainWindow", "GOLDA"))
        self.cmbCity.setItemText(54, _translate("MainWindow", "GORDON"))
        self.cmbCity.setItemText(55, _translate("MainWindow", "GREEN ACRES"))
        self.cmbCity.setItemText(56, _translate("MainWindow", "GREENVIEW SUB."))
        self.cmbCity.setItemText(57, _translate("MainWindow", "HENDRYSBURG"))
        self.cmbCity.setItemText(58, _translate("MainWindow", "HILLCREST SUB."))
        self.cmbCity.setItemText(59, _translate("MainWindow", "HOLLOWAY"))
        self.cmbCity.setItemText(60, _translate("MainWindow", "HOMELAND MANOR"))
        self.cmbCity.setItemText(61, _translate("MainWindow", "HOMESIDE ADD."))
        self.cmbCity.setItemText(62, _translate("MainWindow", "JOHNSON SUB.DIV"))
        self.cmbCity.setItemText(63, _translate("MainWindow", "KIRKWOOD HEIGHTS"))
        self.cmbCity.setItemText(64, _translate("MainWindow", "LA-JAN MEADOWS"))
        self.cmbCity.setItemText(65, _translate("MainWindow", "LAFFERTY"))
        self.cmbCity.setItemText(66, _translate("MainWindow", "LAISLE ADDITION"))
        self.cmbCity.setItemText(67, _translate("MainWindow", "LANSING"))
        self.cmbCity.setItemText(68, _translate("MainWindow", "LLOYDSVILLE"))
        self.cmbCity.setItemText(69, _translate("MainWindow", "LODI ESTATES"))
        self.cmbCity.setItemText(70, _translate("MainWindow", "LOOMIS"))
        self.cmbCity.setItemText(71, _translate("MainWindow", "LYNN ADDITION"))
        self.cmbCity.setItemText(72, _translate("MainWindow", "MARTINS FERRY"))
        self.cmbCity.setItemText(73, _translate("MainWindow", "MCCORKLES ADD."))
        self.cmbCity.setItemText(74, _translate("MainWindow", "MCELWAIN PLACE"))
        self.cmbCity.setItemText(75, _translate("MainWindow", "MIDWAY"))
        self.cmbCity.setItemText(76, _translate("MainWindow", "MIKESINOVICH SUB."))
        self.cmbCity.setItemText(77, _translate("MainWindow", "MONT CLAIR ADD."))
        self.cmbCity.setItemText(78, _translate("MainWindow", "MT. OLIVETT"))
        self.cmbCity.setItemText(79, _translate("MainWindow", "NEW CASTLE"))
        self.cmbCity.setItemText(80, _translate("MainWindow", "NORTH LAWN SUB."))
        self.cmbCity.setItemText(81, _translate("MainWindow", "ORCHARD TERRACE"))
        self.cmbCity.setItemText(82, _translate("MainWindow", "PANORAMA HEIGHTS"))
        self.cmbCity.setItemText(83, _translate("MainWindow", "PATCH"))
        self.cmbCity.setItemText(84, _translate("MainWindow", "PENNWOOD EST."))
        self.cmbCity.setItemText(85, _translate("MainWindow", "PINE LAKE FARMS"))
        self.cmbCity.setItemText(86, _translate("MainWindow", "POWHATAN POINT"))
        self.cmbCity.setItemText(87, _translate("MainWindow", "PULTNEY"))
        self.cmbCity.setItemText(88, _translate("MainWindow", "QUIMBY ADDITION"))
        self.cmbCity.setItemText(89, _translate("MainWindow", "QUINCY"))
        self.cmbCity.setItemText(90, _translate("MainWindow", "RICH ACRES ADD."))
        self.cmbCity.setItemText(91, _translate("MainWindow", "RIDGEVIEW EST."))
        self.cmbCity.setItemText(92, _translate("MainWindow", "ROCK HILL"))
        self.cmbCity.setItemText(93, _translate("MainWindow", "ROLLING HILLS"))
        self.cmbCity.setItemText(94, _translate("MainWindow", "RUSTIC ARMS COM."))
        self.cmbCity.setItemText(95, _translate("MainWindow", "SENORA"))
        self.cmbCity.setItemText(96, _translate("MainWindow", "SEWELLSIVILLE"))
        self.cmbCity.setItemText(97, _translate("MainWindow", "SHADYSIDE"))
        self.cmbCity.setItemText(98, _translate("MainWindow", "SMITH ADDITION"))
        self.cmbCity.setItemText(99, _translate("MainWindow", "SOMERTON"))
        self.cmbCity.setItemText(100, _translate("MainWindow", "SOUTH GATE MANOR"))
        self.cmbCity.setItemText(101, _translate("MainWindow", "SPACEVIEW RIDGE"))
        self.cmbCity.setItemText(102, _translate("MainWindow", "ST. CLAIRSVILLE"))
        self.cmbCity.setItemText(103, _translate("MainWindow", "ST. JOE"))
        self.cmbCity.setItemText(104, _translate("MainWindow", "STEWARTSVILLE"))
        self.cmbCity.setItemText(105, _translate("MainWindow", "STOBBS ESTATES"))
        self.cmbCity.setItemText(106, _translate("MainWindow", "SUMMERHILL ADD."))
        self.cmbCity.setItemText(107, _translate("MainWindow", "SUNNY HILL ACRES"))
        self.cmbCity.setItemText(108, _translate("MainWindow", "SUNNY MEADOWS"))
        self.cmbCity.setItemText(109, _translate("MainWindow", "SUNSET ESTATE"))
        self.cmbCity.setItemText(110, _translate("MainWindow", "TACOMA"))
        self.cmbCity.setItemText(111, _translate("MainWindow", "TEMPERANCEVILLE"))
        self.cmbCity.setItemText(112, _translate("MainWindow", "THEAKER ADD."))
        self.cmbCity.setItemText(113, _translate("MainWindow", "TOMOLONIS SUB."))
        self.cmbCity.setItemText(114, _translate("MainWindow", "UNIONTOWN"))
        self.cmbCity.setItemText(115, _translate("MainWindow", "UPLAND PARK"))
        self.cmbCity.setItemText(116, _translate("MainWindow", "VALLEY VIEW ADD."))
        self.cmbCity.setItemText(117, _translate("MainWindow", "VISTA ESTATES"))
        self.cmbCity.setItemText(118, _translate("MainWindow", "W. LAWN HEIGHTS"))
        self.cmbCity.setItemText(119, _translate("MainWindow", "WARNER'S ADD"))
        self.cmbCity.setItemText(120, _translate("MainWindow", "WASHINGTON HEIGHTS"))
        self.cmbCity.setItemText(121, _translate("MainWindow", "WEGEE"))
        self.cmbCity.setItemText(122, _translate("MainWindow", "WEST BELLAIRE"))
        self.cmbCity.setItemText(123, _translate("MainWindow", "WEST BRIDGEPORT"))
        self.cmbCity.setItemText(124, _translate("MainWindow", "WEST LAWN HGHTS."))
        self.cmbCity.setItemText(125, _translate("MainWindow", "WEST LORETTO"))
        self.cmbCity.setItemText(126, _translate("MainWindow", "WEST WHEELING"))
        self.cmbCity.setItemText(127, _translate("MainWindow", "WILSON"))
        self.cmbCity.setItemText(128, _translate("MainWindow", "WOLFHURST"))
        self.cmbCity.setItemText(129, _translate("MainWindow", "WORELY ADDITION"))
        self.cmbCity.setItemText(130, _translate("MainWindow", "YORKVILLE"))
        self.label_12.setText(_translate("MainWindow", "City"))
        self.cmbMailCity.setItemText(1, _translate("MainWindow", "ADENA"))
        self.cmbMailCity.setItemText(2, _translate("MainWindow", "ALLEDONIA"))
        self.cmbMailCity.setItemText(3, _translate("MainWindow", "BARNESVILLE"))
        self.cmbMailCity.setItemText(4, _translate("MainWindow", "BEALLSVILLE"))
        self.cmbMailCity.setItemText(5, _translate("MainWindow", "BELLAIRE"))
        self.cmbMailCity.setItemText(6, _translate("MainWindow", "BELMONT"))
        self.cmbMailCity.setItemText(7, _translate("MainWindow", "BETHESDA"))
        self.cmbMailCity.setItemText(8, _translate("MainWindow", "BRIDGEPORT"))
        self.cmbMailCity.setItemText(9, _translate("MainWindow", "CADIZ"))
        self.cmbMailCity.setItemText(10, _translate("MainWindow", "DILLONVALE"))
        self.cmbMailCity.setItemText(11, _translate("MainWindow", "FLUSHING"))
        self.cmbMailCity.setItemText(12, _translate("MainWindow", "FREEPORT"))
        self.cmbMailCity.setItemText(13, _translate("MainWindow", "JACOBSBURG"))
        self.cmbMailCity.setItemText(14, _translate("MainWindow", "JERUSALEM"))
        self.cmbMailCity.setItemText(15, _translate("MainWindow", "MARTINS FERRY"))
        self.cmbMailCity.setItemText(16, _translate("MainWindow", "PIEDMONT"))
        self.cmbMailCity.setItemText(17, _translate("MainWindow", "POWHATAN POINT"))
        self.cmbMailCity.setItemText(18, _translate("MainWindow", "QUAKER CITY"))
        self.cmbMailCity.setItemText(19, _translate("MainWindow", "RAYLAND"))
        self.cmbMailCity.setItemText(20, _translate("MainWindow", "ST CLAIRSVILLE"))
        self.cmbMailCity.setItemText(21, _translate("MainWindow", "SHADYSIDE"))
        self.cmbMailCity.setItemText(22, _translate("MainWindow", "WOODSFIELD"))
        self.cmbMailCity.setItemText(23, _translate("MainWindow", "YORKVILLE"))
        self.label_13.setText(_translate("MainWindow", "Mail City"))
        self.cmbComm.setItemText(1, _translate("MainWindow", "ARMSTRONG MILLS"))
        self.cmbComm.setItemText(2, _translate("MainWindow", "AVONDALE"))
        self.cmbComm.setItemText(3, _translate("MainWindow", "BAILEYS MILLS"))
        self.cmbComm.setItemText(4, _translate("MainWindow", "BANNOCK"))
        self.cmbComm.setItemText(5, _translate("MainWindow", "BEL HAVEN"))
        self.cmbComm.setItemText(6, _translate("MainWindow", "BELLE VILLAGE"))
        self.cmbComm.setItemText(7, _translate("MainWindow", "BELLVIEW HEIGHTS"))
        self.cmbComm.setItemText(8, _translate("MainWindow", "BAINE"))
        self.cmbComm.setItemText(9, _translate("MainWindow", "BAINESVILLE"))
        self.cmbComm.setItemText(10, _translate("MainWindow", "BLOOMINGDALE"))
        self.cmbComm.setItemText(11, _translate("MainWindow", "BONAR ALLOT"))
        self.cmbComm.setItemText(12, _translate("MainWindow", "BOSTON"))
        self.cmbComm.setItemText(13, _translate("MainWindow", "BOYDSVILLE"))
        self.cmbComm.setItemText(14, _translate("MainWindow", "BROOKFIELD"))
        self.cmbComm.setItemText(15, _translate("MainWindow", "BROOKVIEW TR"))
        self.cmbComm.setItemText(16, _translate("MainWindow", "BROOKVIEW TR CT"))
        self.cmbComm.setItemText(17, _translate("MainWindow", "BRUESVILLE"))
        self.cmbComm.setItemText(18, _translate("MainWindow", "CANTERBURY EST"))
        self.cmbComm.setItemText(19, _translate("MainWindow", "CAPTORS ADDN"))
        self.cmbComm.setItemText(20, _translate("MainWindow", "CASA-HIJA SUB"))
        self.cmbComm.setItemText(21, _translate("MainWindow", "CENTERVILLE"))
        self.cmbComm.setItemText(22, _translate("MainWindow", "CHERRY FORREST"))
        self.cmbComm.setItemText(23, _translate("MainWindow", "CLARKSBURG"))
        self.cmbComm.setItemText(24, _translate("MainWindow", "COLERAIN"))
        self.cmbComm.setItemText(25, _translate("MainWindow", "CONSERVANCY"))
        self.cmbComm.setItemText(26, _translate("MainWindow", "COUNTRY COURT"))
        self.cmbComm.setItemText(27, _translate("MainWindow", "CRESCENT"))
        self.cmbComm.setItemText(28, _translate("MainWindow", "CRESTVIEW EST"))
        self.cmbComm.setItemText(29, _translate("MainWindow", "CTRY CLUB EST"))
        self.cmbComm.setItemText(30, _translate("MainWindow", "DIX ADDITION"))
        self.cmbComm.setItemText(31, _translate("MainWindow", "DUDEKS ADD"))
        self.cmbComm.setItemText(32, _translate("MainWindow", "EAST LORETTO"))
        self.cmbComm.setItemText(33, _translate("MainWindow", "EAST RICHLAND"))
        self.cmbComm.setItemText(34, _translate("MainWindow", "ECHO"))
        self.cmbComm.setItemText(35, _translate("MainWindow", "EDGE WATER PARK"))
        self.cmbComm.setItemText(36, _translate("MainWindow", "EDGEWATER PARK"))
        self.cmbComm.setItemText(37, _translate("MainWindow", "EVICKS 1ST SUB"))
        self.cmbComm.setItemText(38, _translate("MainWindow", "EVICKS SUB"))
        self.cmbComm.setItemText(39, _translate("MainWindow", "FAIRPOINT"))
        self.cmbComm.setItemText(40, _translate("MainWindow", "FERRYVIEW"))
        self.cmbComm.setItemText(41, _translate("MainWindow", "FLORENCE"))
        self.cmbComm.setItemText(42, _translate("MainWindow", "FOREST GLEN"))
        self.cmbComm.setItemText(43, _translate("MainWindow", "FOX-SHANNON PL"))
        self.label_14.setText(_translate("MainWindow", "Community"))
        self.label_15.setText(_translate("MainWindow", "Subdivision"))
        self.label_16.setText(_translate("MainWindow", "Business Name"))
        self.label_17.setText(_translate("MainWindow", "Township"))
        self.cmbTownship.setItemText(1, _translate("MainWindow", "COLERAIN"))
        self.cmbTownship.setItemText(2, _translate("MainWindow", "FLUSHING"))
        self.cmbTownship.setItemText(3, _translate("MainWindow", "GOSHEN"))
        self.cmbTownship.setItemText(4, _translate("MainWindow", "KIRKWOOD"))
        self.cmbTownship.setItemText(5, _translate("MainWindow", "MEAD"))
        self.cmbTownship.setItemText(6, _translate("MainWindow", "PEASE"))
        self.cmbTownship.setItemText(7, _translate("MainWindow", "PULTNEY"))
        self.cmbTownship.setItemText(8, _translate("MainWindow", "RICHLAND"))
        self.cmbTownship.setItemText(9, _translate("MainWindow", "SMITH"))
        self.cmbTownship.setItemText(10, _translate("MainWindow", "SOMERSET"))
        self.cmbTownship.setItemText(11, _translate("MainWindow", "UNION"))
        self.cmbTownship.setItemText(12, _translate("MainWindow", "WARREN"))
        self.cmbTownship.setItemText(13, _translate("MainWindow", "WASHINGTON"))
        self.cmbTownship.setItemText(14, _translate("MainWindow", "WAYNE"))
        self.cmbTownship.setItemText(15, _translate("MainWindow", "WHEELING"))
        self.cmbTownship.setItemText(16, _translate("MainWindow", "YORK"))
        self.label_18.setText(_translate("MainWindow", "Road #"))
        self.label_19.setText(_translate("MainWindow", "Last Updated"))
        self.cmbESN.setItemText(1, _translate("MainWindow", "740"))
        self.cmbESN.setItemText(2, _translate("MainWindow", "741"))
        self.cmbESN.setItemText(3, _translate("MainWindow", "742"))
        self.cmbESN.setItemText(4, _translate("MainWindow", "743"))
        self.cmbESN.setItemText(5, _translate("MainWindow", "744"))
        self.cmbESN.setItemText(6, _translate("MainWindow", "745"))
        self.cmbESN.setItemText(7, _translate("MainWindow", "746"))
        self.cmbESN.setItemText(8, _translate("MainWindow", "747"))
        self.cmbESN.setItemText(9, _translate("MainWindow", "748"))
        self.cmbESN.setItemText(10, _translate("MainWindow", "749"))
        self.cmbESN.setItemText(11, _translate("MainWindow", "750"))
        self.cmbESN.setItemText(12, _translate("MainWindow", "751"))
        self.cmbESN.setItemText(13, _translate("MainWindow", "752"))
        self.cmbESN.setItemText(14, _translate("MainWindow", "753"))
        self.cmbESN.setItemText(15, _translate("MainWindow", "754"))
        self.cmbESN.setItemText(16, _translate("MainWindow", "755"))
        self.cmbESN.setItemText(17, _translate("MainWindow", "756"))
        self.cmbESN.setItemText(18, _translate("MainWindow", "757"))
        self.cmbESN.setItemText(19, _translate("MainWindow", "758"))
        self.label_20.setText(_translate("MainWindow", "ESN"))
        self.label_21.setText(_translate("MainWindow", "Fire"))
        self.label_22.setText(_translate("MainWindow", "Police"))
        self.label_23.setText(_translate("MainWindow", "EMS"))
        # self.btnUpdate.setText(_translate("MainWindow", "Update"))
        self.btnInsert.setText(_translate("MainWindow", "Update DB"))
        self.btnDel.setText(_translate("MainWindow", "Delete"))
        self.btnMapIt.setText(_translate("MainWindow", "View Map"))
        self.btnClearSearch.setText(_translate("MainWindow", "Clear"))
        self.chkExclude.setText(_translate("MainWindow", "Exclude from update"))
        self.btnNewRecord.setText(_translate("MainWindow", "New Record"))
        self.label_24.setText(_translate("MainWindow", "Belmont County 911 House Numbering Database"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Searching Info"))
        self.label_26.setText(_translate("MainWindow", "Last Name"))
        self.label_27.setText(_translate("MainWindow", "House Number"))
        self.label_28.setText(_translate("MainWindow", "Road Number"))
        self.label_29.setText(_translate("MainWindow", "Road Name"))
        self.lblMapNumSearch.setText(_translate("MainWindow", "Map Number"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Reports"))
        self.btnZeroMapNumReport.setText(_translate("MainWindow", "0 Map#"))
        # self.btnHNMapNumReport.setText(_translate("MainWindow", "HN / Map #"))
        # self.btnESNReport.setText(_translate("MainWindow", "ESN"))
        self.btnDupMapNumReport.setText(_translate("MainWindow", "Dup Map #"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.grpOwnerData.setTitle(_translate("MainWindow", "Owner Data"))
        self.lblEngineers_lname.setText(_translate("MainWindow", "Owner Last Name (Engineer\'s Office)"))
        self.lblEngineers_fname.setText(_translate("MainWindow", "Owner First Name (Engineer\'s Office)"))
        self.lblAuditors_name.setText(_translate("MainWindow", "Owner Name (Auditor\'s Office)"))
        self.lblEngineers_fname_2.setText(_translate("MainWindow", "Parcel Pin"))
        # self.btnUpdate_wEngnr.setText(_translate("MainWindow", "Update w/Engineer Data"))
    def loadMapList(self):
        self.mapNumList = [x[0] for x in self.mapNumList]
        self.cmbMapNum.clear()
        intMapNumList = []
        for x in self.mapNumList:
            if x == '' or x is None:
                pass
            else:
                intMapNumList.append(int(x))
        intMapNumList.sort()
        # self.mapNumList = sorted(self.mapNumList, key=lambda x: int(x))
        # self.mapNumList.sort()
        self.cmbMapNum.addItem("")
        for mapNumItm in intMapNumList:
            self.cmbMapNum.addItem(str(mapNumItm))

        self.TypesOfStreets = list(set(self.TypesOfStreets))
        self.cmbStType.clear()
        self.TypesOfStreets.sort()
        for st_itm in self.TypesOfStreets:
            self.cmbStType.addItems(st_itm)

        self.communityList = list(set(self.communityList))
        self.cmbComm.clear()
        self.cmbComm.addItem(" ")
        self.communityList.sort()
        for commItm in self.communityList:
            self.cmbComm.addItems(commItm)

        self.cmbESN.blockSignals(True)
        self.esnList = list(set(self.esnList))
        self.cmbESN.clear()
        self.esnList.sort()
        for esnItm in self.esnList:
            self.cmbESN.addItems(esnItm)
        self.cmbESN.blockSignals(False)
    def to_upper(self, txtField):
        try:
            itmObj = str(txtField).split()
            mod, kind, fieldType = itmObj[0].split(".")
            if fieldType == "QLineEdit":
                txtField.setText(txtField.text().upper())
            elif fieldType == "QComboBox":
                txtField.setCurrentText(txtField.currentText().upper())
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def streetCheck(self, street):
        try:
            self.c.execute('SELECT id FROM housenum WHERE st_name = ?', (street.strip(),))
            if self.c.fetchone():
                self.txtStreetName.setStyleSheet("QLineEdit { background-color: white;}")
            else:
                self.txtStreetName.setStyleSheet("QLineEdit { background-color: red;}")
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)
            # print("EXCEPTION: {0}".format(e))
    def AddyCheck(self):
        try:
            curAddy = self.txtPreDir.text().strip(),\
                      self.txtStreetName.text().strip(), self.cmbStType.currentText().strip(),\
                      self.txtStreetDir.text().strip()
            curAddy2 =self.txtPreDir.text().strip() + " " +\
                      self.txtStreetName.text().strip() + " " + self.cmbStType.currentText().strip() + " " +\
                      self.txtStreetDir.text().strip()
            self.c.execute('''SELECT pre_dir, st_name, st_type, suf_dir FROM housenum WHERE
                              pre_dir = ? AND st_name = ? AND st_type = ? AND suf_dir = ?''',
                           (self.txtPreDir.text().strip(), self.txtStreetName.text().strip(),
                            self.cmbStType.currentText().strip(), self.txtStreetDir.text().strip()))
            self.c.execute("""SELECT pre_dir, st_name, st_type, suf_dir FROM housenum 
                              WHERE hn_id like '%{}%'""".format(curAddy2))

            if self.c.fetchone():
                self.txtPreDir.setStyleSheet(("QLineEdit { background-color: white;}"))
                self.txtStreetName.setStyleSheet("QLineEdit { background-color: white;}")
                self.cmbStType.setStyleSheet(("QComboBox { background-color: white;}"))
                self.txtStreetDir.setStyleSheet(("QLineEdit { background-color: white;}"))
                # self.txtStreetName.setStyleSheet("QLineEdit { background-color: white;}")
            else:
                self.txtPreDir.setStyleSheet(("QLineEdit { background-color: red;}"))
                self.txtStreetName.setStyleSheet("QLineEdit { background-color: red;}")
                self.cmbStType.setStyleSheet(("QComboBox { background-color: red;}"))
                self.txtStreetDir.setStyleSheet(("QLineEdit { background-color: red;}"))

                # for index, (first, second) in enumerate(zip(dbAddy, curAddy)):
                #     if first != second:
                #         print(index, second)
                # self.txtStreetName.setStyleSheet("QLineEdit { background-color: red;}")
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)
    def esnUpdate(self):
        try:
            self.c.execute('SELECT * FROM esn WHERE esn = ?', (self.cmbESN.currentText(),))
            esnInfo = self.c.fetchall()
            self.txtPolice.setText(esnInfo[0][1])
            self.txtFire.setText(esnInfo[0][2])
            self.txtEMS.setText(esnInfo[0][3])
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def newRecord(self):
        try:
            self.clrFields()
            nextMapNum = self.getMapNum()
            mapNumIndex = self.cmbMapNum.findText(str(nextMapNum))
            if mapNumIndex >= 0:
                self.cmbMapNum.setCurrentIndex(mapNumIndex)
            else:
                self.cmbMapNum.addItem(str(nextMapNum))
                mapNumIndex = self.cmbMapNum.findText(str(nextMapNum))
                self.cmbMapNum.setCurrentIndex(mapNumIndex)

        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def getMapNum(self):
        try:
            intMapNumList = []
            for x in self.mapNumList:
                if x[0] == '' or x[0] is None:
                    pass
                else:
                    intMapNumList.append(int(x[0]))
            intMapNumList.sort()
            Highestnum = intMapNumList[-1]
            nextNum = int(Highestnum) + 1
            return nextNum
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def dbSearch(self, searchItem, field):
        try:
            searchItem.setText(searchItem.text().upper())
            if searchItem.text() == "":
                self.loadData()
            else:
                columnOfInterest = 11
                valueOfInterest = searchItem.text().upper()
                sqlStatment = "SELECT * FROM housenum WHERE " + field + " LIKE '" + valueOfInterest + "%'"
                self.c.execute(sqlStatment)
                searchList = self.c.fetchall()
                self.loadSearch(searchList)
                self.tableWidget.setSortingEnabled(True)
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def zeroMapNumReport(self):
        try:
            self.c.execute("SELECT hn_id, fname, lname, map_no FROM housenum WHERE map_no = 0 ORDER BY hn_id ASC")
            zeroNums = self.c.fetchall()
            mapNum = 0
            mapNumCount = 0
            with open("zeroMapNums.txt", "w")as zeroMapNums_txtFile:
                header = ["HN_ID", "Last Name", "First Name"]
                zeroMapNums_txtFile.write('{0[0]:<60}{0[1]:<60}{0[2]:<5}'.format(header))
                zeroMapNums_txtFile.write("\n\n")
                for x in zeroNums:
                    body = [x[0].strip(), x[2], x[1]]
                    zeroMapNums_txtFile.write('{0[0]:<60}{0[1]:<60}{0[2]:<5}'.format(body))
                    zeroMapNums_txtFile.write("\n")
            os.startfile('zeroMapNums.txt')
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def dupMapReport(self):
        try:
            self.c.execute(
                "SELECT hn_id, fname, lname, map_no FROM housenum WHERE map_no > 0 AND map_no IN (SELECT map_no FROM housenum GROUP BY map_no HAVING COUNT(*)>1) ORDER BY map_no ASC")
            dupMapNums = self.c.fetchall()
            mapNum = 0
            mapNumCount = 0
            with open("DuplicateMapNums.txt", "w")as dupMap_txtFile:
                header = ["Map Number", "HN_ID", "Last Name", "First Name"]
                dupMap_txtFile.write('{0[0]:<60}{0[1]:<40}{0[2]:<60}{0[3]:<40}'.format(header))
                dupMap_txtFile.write("\n\n")
                for x in dupMapNums:
                    if mapNum == 0:
                        mapNum = str(x[3]).strip()
                        dupNumItem = [mapNum, x[0], x[2], x[1]]
                        dupMap_txtFile.write('{0[0]:<60} {0[1]:<40} {0[2]:<60} {0[3]:<40}'.format(dupNumItem))
                        dupMap_txtFile.write("\n")
                        mapNumCount = mapNumCount + 1
                    elif str(mapNum).strip() == str(x[3]).strip():
                        dupNumItem = [x[0], x[2], x[1]]
                        dupMap_txtFile.write('{0[0]:>80} {0[1]:>70} {0[2]:>50}'.format(dupNumItem))
                        dupMap_txtFile.write("\n")
                        mapNumCount = mapNumCount + 1
                    else:
                        mapNum = str(x[3]).strip()
                        dupNumItem = [mapNum, x[0], x[2], x[1]]
                        dupMap_txtFile.write('{0[0]:<60} {0[1]:<40} {0[2]:<60} {0[3]:<40}'.format(dupNumItem))
                        dupMap_txtFile.write("\n")
                        mapNumCount = 1
            os.startfile('DuplicateMapNums.txt')
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def clrFields(self):
        fields = [self.txtLastNameSearch, self.txtHouseNumSearch_2, self.txtRdNumSearch, self.txtRdNameSearch,
                  self.txtMapNumSearch]
        try:
            for field in fields:
                if len(field.text()) > 0:
                    field.blockSignals(True)
                    field.clear()
                    field.blockSignals(False)
            self.reset_items()
            self.loadData()
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def cell_was_clicked(self, row, column):
        try:
            self.txtPreDir.setStyleSheet(("QLineEdit { background-color: white;}"))
            self.txtStreetName.setStyleSheet("QLineEdit { background-color: white;}")
            self.cmbStType.setStyleSheet(("QComboBox { background-color: white;}"))
            self.txtStreetDir.setStyleSheet(("QLineEdit { background-color: white;}"))
            HseNumId = self.tableWidget.item(row, 1)
            self.txtHnID.setText(str(HseNumId.text()))

            HseNumber = self.tableWidget.item(row, 2)
            self.txtHN.setText(str(HseNumber.text()))

            HseSuffix = self.tableWidget.item(row, 3)
            if HseSuffix.text() is None:
                HseSuffix = ""
            self.txtHN_suffix.setText(str(HseSuffix.text()))

            HsePreDir = self.tableWidget.item(row, 4)
            self.txtPreDir.setText(str(HsePreDir.text()))

            StrName = self.tableWidget.item(row, 6)
            self.txtStreetName.setText(str(StrName.text()))

            StrType = self.tableWidget.item(row, 7)
            strTypeIndex = self.cmbStType.findText(StrType.text().strip())
            if strTypeIndex >= 0:
                self.cmbStType.setCurrentIndex(strTypeIndex)

            mapNo = self.tableWidget.item(row, 16)
            mapNoIndex = self.cmbMapNum.findText(mapNo.text().strip())
            if mapNoIndex >= 0:
                self.cmbMapNum.setCurrentIndex(mapNoIndex)

            StrDir = self.tableWidget.item(row, 8)
            self.txtStreetDir.setText(str(StrDir.text()))

            LastName = self.tableWidget.item(row, 12)
            self.txtLastName.setText(str(LastName.text()))

            FirstName = self.tableWidget.item(row, 11)
            self.txtFirstName.setText(str(FirstName.text()))

            Addr2 = self.tableWidget.item(row, 9)
            self.txtLastName_2.setText(str(Addr2.text()))

            City = self.tableWidget.item(row, 10)
            cityIndex = self.cmbCity.findText(City.text().strip())
            if cityIndex >= 0:
                self.cmbCity.setCurrentIndex(cityIndex)

            MailCity = self.tableWidget.item(row, 13)
            MailCityIndex = self.cmbMailCity.findText(MailCity.text().strip())
            if MailCityIndex >= 0:
                self.cmbMailCity.setCurrentIndex(MailCityIndex)

            Community = self.tableWidget.item(row, 19)
            communityIndex = self.cmbComm.findText(Community.text().strip())
            if communityIndex >= 0:
                self.cmbComm.setCurrentIndex(communityIndex)

            Subdiv = self.tableWidget.item(row, 20)
            self.txtSubdiv.setText(str(Subdiv.text()))

            BusiName = self.tableWidget.item(row, 18)
            self.txtBusinessName.setText(str(BusiName.text()))

            Township = self.tableWidget.item(row, 14)
            townshipIndex = self.cmbTownship.findText(Township.text().strip())
            if townshipIndex >= 0:
                self.cmbTownship.setCurrentIndex(townshipIndex)

            roadNumb = self.tableWidget.item(row, 15)
            self.txtRdNum.setText(str(roadNumb.text()))

            dateUpdated = self.tableWidget.item(row, 27)
            dateEdid = str(dateUpdated.text())
            displayDate = QtCore.QDate.fromString(dateEdid, 'yyyy-MM-dd')
            self.dateEdit.setDate(displayDate)

            esn = self.tableWidget.item(row, 17)
            esnIndex = self.cmbESN.findText(esn.text().strip())
            if esnIndex >= 0:
                self.cmbESN.setCurrentIndex(esnIndex)

            Fire = self.tableWidget.item(row, 24)
            self.txtFire.setText(str(Fire.text()))

            Police = self.tableWidget.item(row, 25)
            self.txtPolice.setText(str(Police.text()))

            EMS = self.tableWidget.item(row, 26)
            self.txtEMS.setText(str(EMS.text()))
            self.popOwnerData()

            tableExclude = self.tableWidget.item(row, 29)
            if tableExclude.text() == "1":
                self.chkExclude.setChecked(True)
            else:
                self.chkExclude.setChecked(False)

        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)
            # print("EXCEPTION: {0}".format(e))

    def popOwnerData(self):
        try:
            sql = "SELECT * FROM parcel WHERE map_no = " + str(self.cmbMapNum.currentText())
            self.c.execute(sql)
            ownerData = self.c.fetchone()
            if ownerData is None:
                self.txtLastNameEngnr.setText("NO MATCH")
                self.txtFirstNameEngnr.setText("NO MATCH")
                self.txtNameAuditor.setText("NO MATCH")
                self.txtParcelPin.setText("NO MATCH")
            elif ownerData[3] != '':
                # pin, parNum, lname, fname, name, hn_id, mapNum = str(x).split(",")
                self.txtLastNameEngnr.setText(ownerData[5].strip())
                if ownerData[6] is None:
                    blankOnwerFirstName = ""
                    self.txtFirstNameEngnr.setText(blankOnwerFirstName)
                else:
                    self.txtFirstNameEngnr.setText(ownerData[6].strip())
                self.txtNameAuditor.setText(ownerData[7].strip())
                self.txtParcelPin.setText(ownerData[3].strip())
            else:
                self.txtLastNameEngnr.setText("NO MATCH")
                self.txtFirstNameEngnr.setText("NO MATCH")
                self.txtNameAuditor.setText("NO MATCH")
                self.txtParcelPin.setText("NO MATCH")
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def mapIt_on_click(self):
        try:
            sql = "SELECT parcel_no FROM parcel WHERE map_no = " + str(self.cmbMapNum.currentText())
            self.c.execute(sql)
            parcel2Map = self.c.fetchone()[0]
            urlParts = "https://belcogis.maps.arcgis.com/apps/webappviewer/index.html?id=e2846e4ee2aa4c7f90e2799c384d7a06&search=true&searchextent=true&find="+ parcel2Map
            #urlParts = "http://belmont-oh.bhamaps.com/?PARCEL_NO=" + parcel2Map
            url = QtCore.QUrl(urlParts)
            if parcel2Map:
                QDesktopServices.openUrl(url)
            else:
                pass


        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def deleteIt_on_click(self):
        try:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Are you sure you want to delete this record?")
            msgBox.setWindowTitle("Delete Record?!")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.No)
            msgBox.setEscapeButton(QMessageBox.Close)
            choice = msgBox.exec_()
            if choice == QMessageBox.Yes:
                with self.conn:
                    sql = 'DELETE FROM housenum WHERE hn_id = ?'
                    self.c.execute(sql, (self.txtHnID.text(),))
                self.clrFields()
            else:
                pass

        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)


    def insertIt_on_click(self):
        try:
            if self.chkExclude.isChecked():
                boolExclude = 1
            else:
                boolExclude = 0
            if self.txtStreetName.text() != "" and self.txtLastName.text() != "" and \
                    self.cmbMapNum.currentIndex() != 0:
                self.c.execute('SELECT * FROM housenum WHERE hn_id = ?', (self.txtHnID.text(),))
                data = self.c.fetchone()
                new_HN_id = self.txtHN.text() + " " + self.txtHN_suffix.text() + " " + self.txtPreDir.text() + " " + \
                            self.txtStreetName.text() + " " + self.cmbStType.currentText() + " " + \
                            self.txtStreetDir.text() + " " + self.cmbComm.currentText()
                if data is None:
                    existingMapNum = self.mapNumCheck(self.cmbMapNum.currentText())
                    if existingMapNum is not None:
                        with self.conn:
                            self.c.execute("""UPDATE housenum SET
                                                     hn_id = ? ,  housenum = ? ,  hn_suf = ? ,  pre_dir = ? ,  
                                                     pre_type = ? ,  st_name = ? ,  st_type = ? ,  suf_dir = ? ,  
                                                     addr2 = ? ,  city = ? ,  fname = ? ,  lname = ? , mailcity = ? ,  
                                                     township = ? ,  road_no = ? , map_no = ? ,  esn = ? ,  
                                                     busness_na = ? ,  community = ? ,  subdiv = ? ,  road_name = ? ,  
                                                     direction = ? ,  phone = ? , fire = ? ,  police = ? ,  ems = ? ,  
                                                     date_upda = ? ,  jur = ?, exclude = ? WHERE map_no = ?""",
                                           (new_HN_id, self.txtHN.text(), self.txtHN_suffix.text(),
                                            self.txtPreDir.text(), "", self.txtStreetName.text(),
                                            self.cmbStType.currentText(), self.txtStreetDir.text(),
                                            self.txtLastName_2.text(), self.cmbCity.currentText(),
                                            self.txtFirstName.text(), self.txtLastName.text(),
                                            self.cmbMailCity.currentText(), self.cmbTownship.currentText(),
                                            self.txtRdNum.text(), self.cmbMapNum.currentText(),
                                            self.cmbESN.currentText(), self.txtBusinessName.text(),
                                            self.cmbComm.currentText(),
                                            self.txtSubdiv.text(), self.txtStreetName.text(), self.txtStreetDir.text(),
                                            "PHONE", self.txtFire.text(),
                                            self.txtPolice.text(), self.txtEMS.text(), self.now.toString(Qt.ISODate),
                                            "", boolExclude, self.cmbMapNum.currentText()
                                            )
                                           )
                        if self.txtLastNameSearch.text() == "" and self.txtHouseNumSearch_2.text() == "" and \
                                self.txtRdNumSearch.text() == "" and self.txtRdNameSearch.text() == "" and \
                                self.txtMapNumSearch.text() == "":
                            self.loadData()
                            self.reset_items()
                            self.clrFields()
                            self.loadMapList()
                        elif self.txtLastNameSearch.text() != "":
                            self.dbSearch(self.txtLastNameSearch, "lname")
                        elif self.txtHouseNumSearch_2.text() != "":
                            self.dbSearch(self.txtHouseNumSearch_2, "housenum")
                        elif self.txtRdNumSearch.text() != "":
                            self.dbSearch(self.txtRdNumSearch, "road_no")
                        elif self.txtRdNameSearch.text() != "":
                            self.dbSearch(self.txtRdNameSearch, "st_name")
                        elif self.txtMapNumSearch.text() != "":
                            self.dbSearch(self.txtMapNumSearch, "map_no")
                        else:
                            update_dialog = QtWidgets.QErrorMessage()
                            update_dialog.setWindowTitle("Update Completed!!")
                            update_dialog.showMessage('''Your update has been completed in the database, but the update 
                            will not take effect in the table until you, "Clear" the table.''')
                            update_dialog.exec_()
                    else:
                        with self.conn:
                            self.c.execute("""INSERT INTO housenum(hn_id,  housenum,  hn_suf,  pre_dir,  pre_type,  st_name,  
                            st_type,  suf_dir,  addr2,  city,  fname,  lname, mailcity,  township,  road_no, map_no,  esn,  
                            busness_na,  community,  subdiv,  road_name,  direction,  phone, fire,  police,  ems,  
                            date_upda,  jur, exclude )  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                           (new_HN_id.upper(), self.txtHN.text().upper(), self.txtHN_suffix.text().upper(),
                                            self.txtPreDir.text().upper(), "", self.txtStreetName.text().upper(),
                                            self.cmbStType.currentText().upper(), self.txtStreetDir.text().upper(),
                                            self.txtLastName_2.text().upper(), self.cmbCity.currentText().upper(),
                                            self.txtFirstName.text().upper(), self.txtLastName.text().upper(),
                                            self.cmbMailCity.currentText().upper(), self.cmbTownship.currentText().upper(),
                                            self.txtRdNum.text().upper(), self.cmbMapNum.currentText(),
                                            self.cmbESN.currentText().upper(), self.txtBusinessName.text().upper(),
                                            self.cmbComm.currentText().upper(),
                                            self.txtSubdiv.text(), self.txtStreetName.text(), self.txtStreetDir.text(),
                                            "PHONE", self.txtFire.text(),
                                            self.txtPolice.text().upper(), self.txtEMS.text().upper(),
                                            self.now.toString(Qt.ISODate), "", boolExclude
                                            )
                                           )
                        self.clrFields()
                        self.loadData()
                else:

                        new_HN_id = self.txtHN.text() + " " + self.txtHN_suffix.text() + " " + self.txtPreDir.text() + \
                                    " " + self.txtStreetName.text() + " " + self.cmbStType.currentText() + " " + \
                                    self.txtStreetDir.text() + " " + self.cmbComm.currentText()
                        with self.conn:
                            self.c.execute("""UPDATE housenum SET
                                                     hn_id = ? ,  housenum = ? ,  hn_suf = ? ,  pre_dir = ? ,  
                                                     pre_type = ? ,  st_name = ? ,  st_type = ? ,  suf_dir = ? ,  
                                                     addr2 = ? ,  city = ? ,  fname = ? ,  lname = ? , mailcity = ? ,  
                                                     township = ? ,  road_no = ? , map_no = ? ,  esn = ? ,  
                                                     busness_na = ? ,  community = ? ,  subdiv = ? ,  road_name = ? ,  
                                                     direction = ? ,  phone = ? , fire = ? ,  police = ? ,  ems = ? ,  
                                                     date_upda = ? ,  jur = ?, exclude = ? WHERE hn_id = ?""",
                                           (new_HN_id, self.txtHN.text(), self.txtHN_suffix.text(),
                                            self.txtPreDir.text(), "", self.txtStreetName.text(),
                                            self.cmbStType.currentText(), self.txtStreetDir.text(),
                                            self.txtLastName_2.text(), self.cmbCity.currentText(),
                                            self.txtFirstName.text(), self.txtLastName.text(),
                                            self.cmbMailCity.currentText(), self.cmbTownship.currentText(),
                                            self.txtRdNum.text(), self.cmbMapNum.currentText(),
                                            self.cmbESN.currentText(), self.txtBusinessName.text(),
                                            self.cmbComm.currentText(),
                                            self.txtSubdiv.text(), self.txtStreetName.text(), self.txtStreetDir.text(),
                                            "PHONE", self.txtFire.text(),
                                            self.txtPolice.text(), self.txtEMS.text(), self.now.toString(Qt.ISODate),
                                            "", boolExclude, self.txtHnID.text()
                                            )
                                           )
                        if self.txtLastNameSearch.text() == "" and self.txtHouseNumSearch_2.text() == "" and\
                                self.txtRdNumSearch.text() == "" and self.txtRdNameSearch.text() == "" and\
                                self.txtMapNumSearch.text() == "":
                            self.loadData()
                            self.reset_items()
                            self.clrFields()
                            self.loadMapList()
                        elif self.txtLastNameSearch.text() != "":
                            self.dbSearch(self.txtLastNameSearch, "lname")
                        elif self.txtHouseNumSearch_2.text() != "":
                            self.dbSearch(self.txtHouseNumSearch_2, "housenum")
                        elif self.txtRdNumSearch.text() != "":
                            self.dbSearch(self.txtRdNumSearch, "road_no")
                        elif self.txtRdNameSearch.text() != "":
                            self.dbSearch(self.txtRdNameSearch, "st_name")
                        elif self.txtMapNumSearch.text() != "":
                            self.dbSearch(self.txtMapNumSearch, "map_no")
                        else:
                            update_dialog = QtWidgets.QErrorMessage()
                            update_dialog.setWindowTitle("Update Completed!!")
                            update_dialog.showMessage('''Your update has been completed in the database, but the update 
                            will not take effect in the table until you, "Clear" the table.''')
                            update_dialog.exec_()
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.setWindowTitle("Record Not Selected")
                error_dialog.showMessage('''Please select a record or populate the
                required fields to insert a new record!''')
                error_dialog.exec_()

        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def mapNumCheck(self, mapNumb):
        self.c.execute('SELECT * FROM housenum WHERE map_no = ?', (mapNumb,))
        mapNumberCheck = self.c.fetchone()
        return mapNumberCheck
    def reset_items(self):
        try:
            txtFields = [self.txtLastNameSearch, self.txtHouseNumSearch_2, self.txtRdNumSearch,
                         self.txtRdNameSearch, self.txtHnID, self.txtHN, self.txtHN_suffix,
                         self.txtPreDir, self.txtStreetName, self.txtStreetDir, self.txtLastName_2,
                         self.txtFirstName, self.txtLastName, self.txtRdNum, self.txtBusinessName, self.txtSubdiv,
                         self.txtStreetName, self.txtStreetDir,
                         self.txtFire, self.txtPolice, self.txtEMS, self.txtLastNameEngnr, self.txtFirstNameEngnr,
                         self.txtNameAuditor, self.txtParcelPin]
            cmbFields = [self.cmbStType, self.cmbCity, self.cmbMailCity, self.cmbTownship,
                         self.cmbMapNum, self.cmbComm, self.cmbESN]
            self.cmbESN.blockSignals(True)
            for cmbField in cmbFields:
                cmbField.setCurrentIndex(0)
            self.cmbESN.blockSignals(False)

            for field in txtFields:
                field.clear()
            self.chkExclude.setChecked(False)
            self.dateEdit.setDate(self.now)
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def closeApp(self):
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
