# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 676)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(10, 10, 221, 641))
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vLayout_managerDashboard = QtWidgets.QVBoxLayout()
        self.vLayout_managerDashboard.setObjectName("vLayout_managerDashboard")
        self.label_managerDashboard = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_managerDashboard.setFont(font)
        self.label_managerDashboard.setObjectName("label_managerDashboard")
        self.vLayout_managerDashboard.addWidget(self.label_managerDashboard)
        self.btn_applicantLog = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_applicantLog.setFont(font)
        self.btn_applicantLog.setObjectName("btn_applicantLog")
        self.vLayout_managerDashboard.addWidget(self.btn_applicantLog)
        self.btn_teamMembers = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_teamMembers.setFont(font)
        self.btn_teamMembers.setObjectName("btn_teamMembers")
        self.vLayout_managerDashboard.addWidget(self.btn_teamMembers)
        self.btn_dLeaderInfoBank = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dLeaderInfoBank.setFont(font)
        self.btn_dLeaderInfoBank.setObjectName("btn_dLeaderInfoBank")
        self.vLayout_managerDashboard.addWidget(self.btn_dLeaderInfoBank)
        self.verticalLayout_4.addLayout(self.vLayout_managerDashboard)
        self.vLayout_adminDashboard = QtWidgets.QVBoxLayout()
        self.vLayout_adminDashboard.setObjectName("vLayout_adminDashboard")
        self.label_adminDashboard = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_adminDashboard.setFont(font)
        self.label_adminDashboard.setObjectName("label_adminDashboard")
        self.vLayout_adminDashboard.addWidget(self.label_adminDashboard)
        self.btn_adminAudits = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        self.btn_adminAudits.setFont(font)
        self.btn_adminAudits.setObjectName("btn_adminAudits")
        self.vLayout_adminDashboard.addWidget(self.btn_adminAudits)
        self.btn_adminManagerProfile = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_adminManagerProfile.setFont(font)
        self.btn_adminManagerProfile.setObjectName("btn_adminManagerProfile")
        self.vLayout_adminDashboard.addWidget(self.btn_adminManagerProfile)
        self.verticalLayout_4.addLayout(self.vLayout_adminDashboard)
        spacerItem = QtWidgets.QSpacerItem(20, 385, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.vLayout_logout = QtWidgets.QVBoxLayout()
        self.vLayout_logout.setObjectName("vLayout_logout")
        self.btn_logout = QtWidgets.QPushButton(self.sidebar)
        self.btn_logout.setObjectName("btn_logout")
        self.vLayout_logout.addWidget(self.btn_logout)
        self.verticalLayout_4.addLayout(self.vLayout_logout)
        self.dashboardContent = QtWidgets.QFrame(self.centralwidget)
        self.dashboardContent.setGeometry(QtCore.QRect(240, 10, 841, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboardContent.sizePolicy().hasHeightForWidth())
        self.dashboardContent.setSizePolicy(sizePolicy)
        self.dashboardContent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboardContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboardContent.setObjectName("dashboardContent")
        self.label_greeting = QtWidgets.QLabel(self.dashboardContent)
        self.label_greeting.setGeometry(QtCore.QRect(10, 10, 821, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_greeting.setFont(font)
        self.label_greeting.setObjectName("label_greeting")
        self.layoutWidget = QtWidgets.QWidget(self.dashboardContent)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 52, 821, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gLayout_chartsAndTables = QtWidgets.QGridLayout(self.layoutWidget)
        self.gLayout_chartsAndTables.setContentsMargins(0, 0, 0, 0)
        self.gLayout_chartsAndTables.setObjectName("gLayout_chartsAndTables")
        self.tbl_latestUpdates = QtWidgets.QTableView(self.layoutWidget)
        self.tbl_latestUpdates.setObjectName("tbl_latestUpdates")
        self.gLayout_chartsAndTables.addWidget(self.tbl_latestUpdates, 1, 0, 1, 1)
        self.chart_memberStats = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_memberStats.sizePolicy().hasHeightForWidth())
        self.chart_memberStats.setSizePolicy(sizePolicy)
        self.chart_memberStats.setObjectName("chart_memberStats")
        self.gLayout_chartsAndTables.addWidget(self.chart_memberStats, 1, 1, 1, 1)
        self.label_latestUpdates = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_latestUpdates.setFont(font)
        self.label_latestUpdates.setObjectName("label_latestUpdates")
        self.gLayout_chartsAndTables.addWidget(self.label_latestUpdates, 0, 0, 1, 1)
        self.label_memberStats = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_memberStats.setFont(font)
        self.label_memberStats.setObjectName("label_memberStats")
        self.gLayout_chartsAndTables.addWidget(self.label_memberStats, 0, 1, 1, 1)
        self.label_pendingApplications = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_pendingApplications.setFont(font)
        self.label_pendingApplications.setObjectName("label_pendingApplications")
        self.gLayout_chartsAndTables.addWidget(self.label_pendingApplications, 2, 0, 1, 1)
        self.tbl_pendingApplications = QtWidgets.QTableView(self.layoutWidget)
        self.tbl_pendingApplications.setObjectName("tbl_pendingApplications")
        self.gLayout_chartsAndTables.addWidget(self.tbl_pendingApplications, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manager Dashboard"))
        self.label_managerDashboard.setText(_translate("MainWindow", "Manager Dashboard"))
        self.btn_applicantLog.setText(_translate("MainWindow", "Applicant Log"))
        self.btn_teamMembers.setText(_translate("MainWindow", "Team Members"))
        self.btn_dLeaderInfoBank.setText(_translate("MainWindow", "DLeader Info Bank"))
        self.label_adminDashboard.setText(_translate("MainWindow", "Administrator Dashboard"))
        self.btn_adminAudits.setText(_translate("MainWindow", "View Latest Audits"))
        self.btn_adminManagerProfile.setText(_translate("MainWindow", "View Manager Profiles"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.label_greeting.setText(_translate("MainWindow", "Greetings!"))
        self.label_latestUpdates.setText(_translate("MainWindow", "Latest Updates"))
        self.label_memberStats.setText(_translate("MainWindow", "Membership Statistics"))
        self.label_pendingApplications.setText(_translate("MainWindow", "Pending Applications"))
