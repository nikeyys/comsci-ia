# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerDLeaderProfile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 496)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hLayout_dLeaderName = QtWidgets.QHBoxLayout()
        self.hLayout_dLeaderName.setObjectName("hLayout_dLeaderName")
        self.label_dLeaderName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_dLeaderName.setFont(font)
        self.label_dLeaderName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_dLeaderName.setObjectName("label_dLeaderName")
        self.hLayout_dLeaderName.addWidget(self.label_dLeaderName)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_dLeaderName.addItem(spacerItem)
        self.btn_editProfile = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editProfile.sizePolicy().hasHeightForWidth())
        self.btn_editProfile.setSizePolicy(sizePolicy)
        self.btn_editProfile.setObjectName("btn_editProfile")
        self.hLayout_dLeaderName.addWidget(self.btn_editProfile)
        self.verticalLayout.addLayout(self.hLayout_dLeaderName)
        self.hLayout_dLeaderInfo = QtWidgets.QHBoxLayout()
        self.hLayout_dLeaderInfo.setObjectName("hLayout_dLeaderInfo")
        self.vLayout_dLeaderID = QtWidgets.QVBoxLayout()
        self.vLayout_dLeaderID.setObjectName("vLayout_dLeaderID")
        self.label_dLeaderID_header = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dLeaderID_header.setFont(font)
        self.label_dLeaderID_header.setObjectName("label_dLeaderID_header")
        self.vLayout_dLeaderID.addWidget(self.label_dLeaderID_header)
        self.label_dLeaderID_filler = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_dLeaderID_filler.setFont(font)
        self.label_dLeaderID_filler.setObjectName("label_dLeaderID_filler")
        self.vLayout_dLeaderID.addWidget(self.label_dLeaderID_filler)
        self.hLayout_dLeaderInfo.addLayout(self.vLayout_dLeaderID)
        spacerItem1 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_dLeaderInfo.addItem(spacerItem1)
        self.vLayout_mobileNumber = QtWidgets.QVBoxLayout()
        self.vLayout_mobileNumber.setObjectName("vLayout_mobileNumber")
        self.label_mobileNumber_header = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_mobileNumber_header.setFont(font)
        self.label_mobileNumber_header.setObjectName("label_mobileNumber_header")
        self.vLayout_mobileNumber.addWidget(self.label_mobileNumber_header)
        self.label_mobileNumber_filler = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_mobileNumber_filler.setFont(font)
        self.label_mobileNumber_filler.setObjectName("label_mobileNumber_filler")
        self.vLayout_mobileNumber.addWidget(self.label_mobileNumber_filler)
        self.hLayout_dLeaderInfo.addLayout(self.vLayout_mobileNumber)
        spacerItem2 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_dLeaderInfo.addItem(spacerItem2)
        self.vLayout_email = QtWidgets.QVBoxLayout()
        self.vLayout_email.setObjectName("vLayout_email")
        self.label_email_header = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_email_header.setFont(font)
        self.label_email_header.setObjectName("label_email_header")
        self.vLayout_email.addWidget(self.label_email_header)
        self.label_email_filler = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_email_filler.setFont(font)
        self.label_email_filler.setObjectName("label_email_filler")
        self.vLayout_email.addWidget(self.label_email_filler)
        self.hLayout_dLeaderInfo.addLayout(self.vLayout_email)
        self.verticalLayout.addLayout(self.hLayout_dLeaderInfo)
        self.tbl_dMembers = QtWidgets.QTableView(self.layoutWidget)
        self.tbl_dMembers.setObjectName("tbl_dMembers")
        self.verticalLayout.addWidget(self.tbl_dMembers)
        self.btn_sendEmail = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_sendEmail.setObjectName("btn_sendEmail")
        self.verticalLayout.addWidget(self.btn_sendEmail)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.btn_close = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_close.setObjectName("btn_close")
        self.verticalLayout.addWidget(self.btn_close)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_dLeaderName.setText(_translate("MainWindow", "LAST NAME, First Name"))
        self.btn_editProfile.setText(_translate("MainWindow", "Edit Profile"))
        self.label_dLeaderID_header.setText(_translate("MainWindow", "DLeader ID"))
        self.label_dLeaderID_filler.setText(_translate("MainWindow", "[DLEADER ID]"))
        self.label_mobileNumber_header.setText(_translate("MainWindow", "Mobile Number"))
        self.label_mobileNumber_filler.setText(_translate("MainWindow", "[MOBILE NUMBER]"))
        self.label_email_header.setText(_translate("MainWindow", "Email Address"))
        self.label_email_filler.setText(_translate("MainWindow", "[EMAIL]"))
        self.btn_sendEmail.setText(_translate("MainWindow", "Send Email"))
        self.btn_close.setText(_translate("MainWindow", "Close"))
