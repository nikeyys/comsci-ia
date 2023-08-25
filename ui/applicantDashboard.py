# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applicantDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 86))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vLayout_applicantInfo = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayout_applicantInfo.setContentsMargins(0, 0, 0, 0)
        self.vLayout_applicantInfo.setObjectName("vLayout_applicantInfo")
        self.label_applicantName = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_applicantName.sizePolicy().hasHeightForWidth())
        self.label_applicantName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_applicantName.setFont(font)
        self.label_applicantName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_applicantName.setObjectName("label_applicantName")
        self.vLayout_applicantInfo.addWidget(self.label_applicantName)
        self.label_applicantID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_applicantID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_applicantID.setObjectName("label_applicantID")
        self.vLayout_applicantInfo.addWidget(self.label_applicantID)
        self.label_dLeader = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_dLeader.setObjectName("label_dLeader")
        self.vLayout_applicantInfo.addWidget(self.label_dLeader)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 10, 241, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vLayout_personalDetails = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayout_personalDetails.setContentsMargins(0, 0, 0, 0)
        self.vLayout_personalDetails.setObjectName("vLayout_personalDetails")
        self.label_personalDetailsHeader = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_personalDetailsHeader.setFont(font)
        self.label_personalDetailsHeader.setObjectName("label_personalDetailsHeader")
        self.vLayout_personalDetails.addWidget(self.label_personalDetailsHeader)
        self.label_mobileNumber = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_mobileNumber.setObjectName("label_mobileNumber")
        self.vLayout_personalDetails.addWidget(self.label_mobileNumber)
        self.label_emailAddress = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_emailAddress.setObjectName("label_emailAddress")
        self.vLayout_personalDetails.addWidget(self.label_emailAddress)
        self.label_dob = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_dob.setObjectName("label_dob")
        self.vLayout_personalDetails.addWidget(self.label_dob)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 150, 571, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.vLayout_pastApplications = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vLayout_pastApplications.setContentsMargins(0, 0, 0, 0)
        self.vLayout_pastApplications.setObjectName("vLayout_pastApplications")
        self.label_prevApplicationsHeader = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_prevApplicationsHeader.setFont(font)
        self.label_prevApplicationsHeader.setObjectName("label_prevApplicationsHeader")
        self.vLayout_pastApplications.addWidget(self.label_prevApplicationsHeader)
        self.tbl_prevApplications = QtWidgets.QTableView(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        self.tbl_prevApplications.setFont(font)
        self.tbl_prevApplications.setObjectName("tbl_prevApplications")
        self.vLayout_pastApplications.addWidget(self.tbl_prevApplications)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 550, 571, 27))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hLayout_additionalButtons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hLayout_additionalButtons.setContentsMargins(0, 0, 0, 0)
        self.hLayout_additionalButtons.setObjectName("hLayout_additionalButtons")
        self.btn_newApplication = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_newApplication.setObjectName("btn_newApplication")
        self.hLayout_additionalButtons.addWidget(self.btn_newApplication)
        self.btn_logout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_logout.setObjectName("btn_logout")
        self.hLayout_additionalButtons.addWidget(self.btn_logout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Applicant Dashboard"))
        self.label_applicantName.setText(_translate("MainWindow", "LAST, First Name"))
        self.label_applicantID.setText(_translate("MainWindow", "Applicant ID: "))
        self.label_dLeader.setText(_translate("MainWindow", "DLeader: "))
        self.label_personalDetailsHeader.setText(_translate("MainWindow", "Personal Details"))
        self.label_mobileNumber.setText(_translate("MainWindow", "Mobile Number:"))
        self.label_emailAddress.setText(_translate("MainWindow", "Email Address:"))
        self.label_dob.setText(_translate("MainWindow", "Date of Birth: "))
        self.label_prevApplicationsHeader.setText(_translate("MainWindow", "Previous Applications"))
        self.btn_newApplication.setText(_translate("MainWindow", "Submit another application"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
