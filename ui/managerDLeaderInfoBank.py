# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerDLeaderInfoBank.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 474)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 611, 441))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_dLeaderInfoBank = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_dLeaderInfoBank.setFont(font)
        self.label_dLeaderInfoBank.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dLeaderInfoBank.setObjectName("label_dLeaderInfoBank")
        self.verticalLayout.addWidget(self.label_dLeaderInfoBank)
        self.hLayout_search = QtWidgets.QHBoxLayout()
        self.hLayout_search.setObjectName("hLayout_search")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_search.addItem(spacerItem)
        self.label_search = QtWidgets.QLabel(self.widget)
        self.label_search.setObjectName("label_search")
        self.hLayout_search.addWidget(self.label_search)
        self.line_searchBar = QtWidgets.QLineEdit(self.widget)
        self.line_searchBar.setObjectName("line_searchBar")
        self.hLayout_search.addWidget(self.line_searchBar)
        self.verticalLayout.addLayout(self.hLayout_search)
        self.tbl_dLeaderTable = QtWidgets.QTableView(self.widget)
        self.tbl_dLeaderTable.setObjectName("tbl_dLeaderTable")
        self.verticalLayout.addWidget(self.tbl_dLeaderTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_addNewDLeader = QtWidgets.QPushButton(self.widget)
        self.btn_addNewDLeader.setObjectName("btn_addNewDLeader")
        self.horizontalLayout.addWidget(self.btn_addNewDLeader)
        self.btn_removeDLeader = QtWidgets.QPushButton(self.widget)
        self.btn_removeDLeader.setObjectName("btn_removeDLeader")
        self.horizontalLayout.addWidget(self.btn_removeDLeader)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_backToDashboard = QtWidgets.QPushButton(self.widget)
        self.btn_backToDashboard.setObjectName("btn_backToDashboard")
        self.verticalLayout.addWidget(self.btn_backToDashboard)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_dLeaderInfoBank.setText(_translate("MainWindow", "DLeader Information Bank"))
        self.label_search.setText(_translate("MainWindow", "Search:"))
        self.btn_addNewDLeader.setText(_translate("MainWindow", "Add New DLeader"))
        self.btn_removeDLeader.setText(_translate("MainWindow", "Remove DLeader"))
        self.btn_backToDashboard.setText(_translate("MainWindow", "Back to Dashboard"))
