# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(360, 30, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.in_send = QtWidgets.QPushButton(self.centralwidget)
        self.in_send.setGeometry(QtCore.QRect(180, 290, 91, 41))
        self.in_send.setObjectName("in_send")
        self.in_show = QtWidgets.QLineEdit(self.centralwidget)
        self.in_show.setGeometry(QtCore.QRect(180, 340, 91, 20))
        self.in_show.setObjectName("in_show")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 140, 406, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_sname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.in_sname.setObjectName("in_sname")
        self.gridLayout.addWidget(self.in_sname, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.in_fname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.in_fname.setObjectName("in_fname")
        self.gridLayout.addWidget(self.in_fname, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.in_com = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.in_com.setObjectName("in_com")
        self.horizontalLayout.addWidget(self.in_com)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.in_platoon = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.in_platoon.setObjectName("in_platoon")
        self.horizontalLayout.addWidget(self.in_platoon)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.in_quater = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.in_quater.setObjectName("in_quater")
        self.gridLayout_2.addWidget(self.in_quater, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        self.in_position = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.in_position.setObjectName("in_position")
        self.gridLayout_2.addWidget(self.in_position, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.out_show = QtWidgets.QLineEdit(self.centralwidget)
        self.out_show.setGeometry(QtCore.QRect(640, 340, 91, 20))
        self.out_show.setText("")
        self.out_show.setObjectName("out_show")
        self.out_send = QtWidgets.QPushButton(self.centralwidget)
        self.out_send.setGeometry(QtCore.QRect(640, 290, 91, 41))
        self.out_send.setObjectName("out_send")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(490, 140, 406, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.out_sname = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.out_sname.setObjectName("out_sname")
        self.gridLayout_3.addWidget(self.out_sname, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.out_fname = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.out_fname.setObjectName("out_fname")
        self.gridLayout_3.addWidget(self.out_fname, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.out_com = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.out_com.setObjectName("out_com")
        self.horizontalLayout_2.addWidget(self.out_com)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.out_platoon = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.out_platoon.setObjectName("out_platoon")
        self.horizontalLayout_2.addWidget(self.out_platoon)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.out_quater = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.out_quater.setObjectName("out_quater")
        self.gridLayout_4.addWidget(self.out_quater, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 1, 1, 1)
        self.out_position = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.out_position.setObjectName("out_position")
        self.gridLayout_4.addWidget(self.out_position, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Security Duty"))
        self.in_send.setText(_translate("MainWindow", "Check In"))
        self.label_2.setText(_translate("MainWindow", "Firstname"))
        self.label_3.setText(_translate("MainWindow", "Surname"))
        self.label_7.setText(_translate("MainWindow", "Company"))
        self.label_8.setText(_translate("MainWindow", "Platoon"))
        self.label_4.setText(_translate("MainWindow", "quater"))
        self.label_5.setText(_translate("MainWindow", "Position"))
        self.out_send.setText(_translate("MainWindow", "Check Out"))
        self.label_10.setText(_translate("MainWindow", "Firstname"))
        self.label_12.setText(_translate("MainWindow", "Surname"))
        self.label_13.setText(_translate("MainWindow", "Company"))
        self.label_14.setText(_translate("MainWindow", "Platoon"))
        self.label_15.setText(_translate("MainWindow", "quater"))
        self.label_16.setText(_translate("MainWindow", "Position"))
#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////
        self.in_send.clicked.connect(self.checkin)
        self.out_send.clicked.connect(self.checkout)
        
    def checkin(self):
        quater = self.in_quater.text()
        fname = self.in_fname.text()
        sname = self.in_sname.text()
        com = self.in_com.text()
        platoon = self.in_platoon.text()
        position = self.in_position.text()
        onduty = 1
        outduty = 0
        upstatus(quater,fname,sname,com,platoon,position)
        uplogin(quater,position,fname,sname,onduty,outduty)
        self.in_show.setPlaceholderText("complete")
        
    def checkout(self):
        quater = self.out_quater.text()
        fname = self.out_fname.text()
        sname = self.out_sname.text()
        com = self.out_com.text()
        platoon = self.out_platoon.text()
        position = self.out_position.text()
        onduty = 0
        outduty = 1
        upstatus(quater,fname,sname,com,platoon,position)
        uplogin(quater,position,fname,sname,onduty,outduty)
        self.out_show.setPlaceholderText("complete")
        
#db
import mysql.connector

def ConnectorMysql():
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="security",
        # auth_plugin='mysql_native_password'
    )
    print("db run")
    return mydb

def upstatus(quater,fname,sname,com,platoon,position):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("UPDATE securestatus SET quater = %s ,fname = %s ,sname = %s ,company = %s ,platoon = %s WHERE position = %s")
    val = (quater,fname,sname,com,platoon,position)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()
    
def uplogin(quater,position,fname,sname,onduty,outduty):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("INSERT INTO securelog (`quater`, `position`, `fname`, `sname`, `onduty`, `outduty`) VALUES (%s , %s , %s , %s , %s , %s) ")
    val = (quater,position,fname,sname,onduty,outduty)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()
    
def uplogout(quater,position,fname,sname,onduty,outduty):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("INSERT INTO securelog (`quater`, `position`, `fname`, `sname`, `outduty`, `outduty`) VALUES (%s , %s , %s , %s , %s , %s) ")
    val = (quater,position,fname,sname,onduty,outduty)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
