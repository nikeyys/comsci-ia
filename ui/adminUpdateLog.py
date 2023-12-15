# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminUpdateLog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vLayout_updateLog = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vLayout_updateLog.setContentsMargins(0, 0, 0, 0)
        self.vLayout_updateLog.setObjectName("vLayout_updateLog")
        self.lbl_recentUpdates = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_recentUpdates.setFont(font)
        self.lbl_recentUpdates.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_recentUpdates.setObjectName("lbl_recentUpdates")
        self.vLayout_updateLog.addWidget(self.lbl_recentUpdates)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.vLayout_updateLog.addItem(spacerItem)
        self.vLayout_options = QtWidgets.QVBoxLayout()
        self.vLayout_options.setObjectName("vLayout_options")
        self.hLayout_searchSort = QtWidgets.QHBoxLayout()
        self.hLayout_searchSort.setObjectName("hLayout_searchSort")
        self.lbl_search = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_search.setObjectName("lbl_search")
        self.hLayout_searchSort.addWidget(self.lbl_search)
        self.ln_searchBar = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_searchBar.sizePolicy().hasHeightForWidth())
        self.ln_searchBar.setSizePolicy(sizePolicy)
        self.ln_searchBar.setMinimumSize(QtCore.QSize(220, 0))
        self.ln_searchBar.setObjectName("ln_searchBar")
        self.hLayout_searchSort.addWidget(self.ln_searchBar)
        spacerItem1 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_searchSort.addItem(spacerItem1)
        self.lbl_sort = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_sort.setObjectName("lbl_sort")
        self.hLayout_searchSort.addWidget(self.lbl_sort)
        self.combo_sort = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_sort.sizePolicy().hasHeightForWidth())
        self.combo_sort.setSizePolicy(sizePolicy)
        self.combo_sort.setObjectName("combo_sort")
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.hLayout_searchSort.addWidget(self.combo_sort)
        self.vLayout_options.addLayout(self.hLayout_searchSort)
        self.hLayout_filter = QtWidgets.QHBoxLayout()
        self.hLayout_filter.setObjectName("hLayout_filter")
        spacerItem2 = QtWidgets.QSpacerItem(515, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_filter.addItem(spacerItem2)
        self.lbl_filteraction = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_filteraction.sizePolicy().hasHeightForWidth())
        self.lbl_filteraction.setSizePolicy(sizePolicy)
        self.lbl_filteraction.setObjectName("lbl_filteraction")
        self.hLayout_filter.addWidget(self.lbl_filteraction)
        self.combo_filterAction = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_filterAction.setEditable(False)
        self.combo_filterAction.setMaxVisibleItems(10)
        self.combo_filterAction.setObjectName("combo_filterAction")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.combo_filterAction.addItem("")
        self.hLayout_filter.addWidget(self.combo_filterAction)
        self.vLayout_options.addLayout(self.hLayout_filter)
        self.vLayout_updateLog.addLayout(self.vLayout_options)
        self.tbl_updateLog = QtWidgets.QTableView(self.layoutWidget)
        self.tbl_updateLog.setObjectName("tbl_updateLog")
        self.vLayout_updateLog.addWidget(self.tbl_updateLog)
        self.btn_backToDashboard = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_backToDashboard.setObjectName("btn_backToDashboard")
        self.vLayout_updateLog.addWidget(self.btn_backToDashboard)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update Log"))
        self.lbl_recentUpdates.setText(_translate("MainWindow", "Update Log"))
        self.lbl_search.setText(_translate("MainWindow", "Search:"))
        self.lbl_sort.setText(_translate("MainWindow", "Sort by:"))
        self.combo_sort.setItemText(0, _translate("MainWindow", "Most Recent Updates"))
        self.combo_sort.setItemText(1, _translate("MainWindow", "Oldest Updates"))
        self.lbl_filteraction.setText(_translate("MainWindow", "Filter by:"))
        self.combo_filterAction.setItemText(0, _translate("MainWindow", "No Filter"))
        self.combo_filterAction.setItemText(1, _translate("MainWindow", "New Member Added"))
        self.combo_filterAction.setItemText(2, _translate("MainWindow", "Member Profile Edited"))
        self.combo_filterAction.setItemText(3, _translate("MainWindow", "Member Removed from DLeader"))
        self.combo_filterAction.setItemText(4, _translate("MainWindow", "Member Added to DLeader"))
        self.combo_filterAction.setItemText(5, _translate("MainWindow", "Member Deleted"))
        self.combo_filterAction.setItemText(6, _translate("MainWindow", "New DLeader Added"))
        self.combo_filterAction.setItemText(7, _translate("MainWindow", "DLeader Profile Edited"))
        self.combo_filterAction.setItemText(8, _translate("MainWindow", "DLeader Deleted"))
        self.combo_filterAction.setItemText(9, _translate("MainWindow", "New Manager Added"))
        self.combo_filterAction.setItemText(10, _translate("MainWindow", "Manager Deleted"))
        self.combo_filterAction.setItemText(11, _translate("MainWindow", "New Application Submitted"))
        self.combo_filterAction.setItemText(12, _translate("MainWindow", "Applicant Account Created"))
        self.combo_filterAction.setItemText(13, _translate("MainWindow", "Applicant Deleted"))
        self.btn_backToDashboard.setText(_translate("MainWindow", "Back to Dashboard"))
