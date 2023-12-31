# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applicantDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 702)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 671))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vLayout_container = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vLayout_container.setContentsMargins(0, 0, 0, 0)
        self.vLayout_container.setObjectName("vLayout_container")
        self.vLayout_applicantInfo = QtWidgets.QVBoxLayout()
        self.vLayout_applicantInfo.setObjectName("vLayout_applicantInfo")
        self.lbl_applicantName = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_applicantName.sizePolicy().hasHeightForWidth())
        self.lbl_applicantName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_applicantName.setFont(font)
        self.lbl_applicantName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_applicantName.setObjectName("lbl_applicantName")
        self.vLayout_applicantInfo.addWidget(self.lbl_applicantName)
        self.hLayout_applicantID = QtWidgets.QHBoxLayout()
        self.hLayout_applicantID.setObjectName("hLayout_applicantID")
        self.lbl_applicantID_header = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_applicantID_header.sizePolicy().hasHeightForWidth())
        self.lbl_applicantID_header.setSizePolicy(sizePolicy)
        self.lbl_applicantID_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_applicantID_header.setObjectName("lbl_applicantID_header")
        self.hLayout_applicantID.addWidget(self.lbl_applicantID_header)
        self.lbl_applicantID_filler = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_applicantID_filler.setObjectName("lbl_applicantID_filler")
        self.hLayout_applicantID.addWidget(self.lbl_applicantID_filler)
        self.vLayout_applicantInfo.addLayout(self.hLayout_applicantID)
        self.hLayout_dleader = QtWidgets.QHBoxLayout()
        self.hLayout_dleader.setObjectName("hLayout_dleader")
        self.lbl_dleader_header = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dleader_header.sizePolicy().hasHeightForWidth())
        self.lbl_dleader_header.setSizePolicy(sizePolicy)
        self.lbl_dleader_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_dleader_header.setObjectName("lbl_dleader_header")
        self.hLayout_dleader.addWidget(self.lbl_dleader_header)
        self.lbl_dleader_filler = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dleader_filler.setObjectName("lbl_dleader_filler")
        self.hLayout_dleader.addWidget(self.lbl_dleader_filler)
        self.vLayout_applicantInfo.addLayout(self.hLayout_dleader)
        self.vLayout_container.addLayout(self.vLayout_applicantInfo)
        self.vLayout_personalDetails = QtWidgets.QVBoxLayout()
        self.vLayout_personalDetails.setObjectName("vLayout_personalDetails")
        self.lbl_personalDetailsHeader = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_personalDetailsHeader.setFont(font)
        self.lbl_personalDetailsHeader.setObjectName("lbl_personalDetailsHeader")
        self.vLayout_personalDetails.addWidget(self.lbl_personalDetailsHeader)
        self.hLayout_mobileNumber = QtWidgets.QHBoxLayout()
        self.hLayout_mobileNumber.setObjectName("hLayout_mobileNumber")
        self.lbl_mobileNumber_header = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_mobileNumber_header.sizePolicy().hasHeightForWidth())
        self.lbl_mobileNumber_header.setSizePolicy(sizePolicy)
        self.lbl_mobileNumber_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_mobileNumber_header.setObjectName("lbl_mobileNumber_header")
        self.hLayout_mobileNumber.addWidget(self.lbl_mobileNumber_header)
        self.lbl_mobileNumber_filler = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_mobileNumber_filler.setObjectName("lbl_mobileNumber_filler")
        self.hLayout_mobileNumber.addWidget(self.lbl_mobileNumber_filler)
        self.vLayout_personalDetails.addLayout(self.hLayout_mobileNumber)
        self.hLayout_email = QtWidgets.QHBoxLayout()
        self.hLayout_email.setObjectName("hLayout_email")
        self.lbl_email_header = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_email_header.sizePolicy().hasHeightForWidth())
        self.lbl_email_header.setSizePolicy(sizePolicy)
        self.lbl_email_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_email_header.setObjectName("lbl_email_header")
        self.hLayout_email.addWidget(self.lbl_email_header)
        self.lbl_email_filler = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_email_filler.setObjectName("lbl_email_filler")
        self.hLayout_email.addWidget(self.lbl_email_filler)
        self.vLayout_personalDetails.addLayout(self.hLayout_email)
        self.hLayout_dob = QtWidgets.QHBoxLayout()
        self.hLayout_dob.setObjectName("hLayout_dob")
        self.lbl_dob_header = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dob_header.sizePolicy().hasHeightForWidth())
        self.lbl_dob_header.setSizePolicy(sizePolicy)
        self.lbl_dob_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_dob_header.setObjectName("lbl_dob_header")
        self.hLayout_dob.addWidget(self.lbl_dob_header)
        self.lbl_dob_filler = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dob_filler.setObjectName("lbl_dob_filler")
        self.hLayout_dob.addWidget(self.lbl_dob_filler)
        self.vLayout_personalDetails.addLayout(self.hLayout_dob)
        self.vLayout_container.addLayout(self.vLayout_personalDetails)
        self.vLayout_pastApplications = QtWidgets.QVBoxLayout()
        self.vLayout_pastApplications.setObjectName("vLayout_pastApplications")
        self.lbl_previousApplicationsHeader = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_previousApplicationsHeader.setFont(font)
        self.lbl_previousApplicationsHeader.setObjectName("lbl_previousApplicationsHeader")
        self.vLayout_pastApplications.addWidget(self.lbl_previousApplicationsHeader)
        self.tbl_prevApplications = QtWidgets.QTableView(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        self.tbl_prevApplications.setFont(font)
        self.tbl_prevApplications.setObjectName("tbl_prevApplications")
        self.vLayout_pastApplications.addWidget(self.tbl_prevApplications)
        self.btn_newApplication = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_newApplication.setObjectName("btn_newApplication")
        self.vLayout_pastApplications.addWidget(self.btn_newApplication)
        self.vLayout_container.addLayout(self.vLayout_pastApplications)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.vLayout_container.addItem(spacerItem)
        self.hLayout_additionalButtons = QtWidgets.QHBoxLayout()
        self.hLayout_additionalButtons.setObjectName("hLayout_additionalButtons")
        self.btn_logout = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_logout.setObjectName("btn_logout")
        self.hLayout_additionalButtons.addWidget(self.btn_logout)
        self.vLayout_container.addLayout(self.hLayout_additionalButtons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Applicant Dashboard"))
        self.lbl_applicantName.setText(_translate("MainWindow", "LAST, First Name"))
        self.lbl_applicantID_header.setText(_translate("MainWindow", "Applicant ID: "))
        self.lbl_applicantID_filler.setText(_translate("MainWindow", "[APPLICANT ID]"))
        self.lbl_dleader_header.setText(_translate("MainWindow", "Discipleship Leader"))
        self.lbl_dleader_filler.setText(_translate("MainWindow", "[DLEADER]"))
        self.lbl_personalDetailsHeader.setText(_translate("MainWindow", "Personal Details"))
        self.lbl_mobileNumber_header.setText(_translate("MainWindow", "Mobile Number:"))
        self.lbl_mobileNumber_filler.setText(_translate("MainWindow", "[MOBILE NUMBER]"))
        self.lbl_email_header.setText(_translate("MainWindow", "Email Address:"))
        self.lbl_email_filler.setText(_translate("MainWindow", "[EMAIL ADDRESS]"))
        self.lbl_dob_header.setText(_translate("MainWindow", "Date of Birth:"))
        self.lbl_dob_filler.setText(_translate("MainWindow", "[DOB]"))
        self.lbl_previousApplicationsHeader.setText(_translate("MainWindow", "Previous Applications"))
        self.btn_newApplication.setText(_translate("MainWindow", "Submit another application"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
