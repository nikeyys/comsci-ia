import random
import re  # regex
import sys

from PyQt5.QtChart import QChart, QBarSeries, QBarSet, QBarCategoryAxis, QChartView
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication

from classes.dialogBoxes import *
from classes.object import *
from classes.tableModel import *
from classes.sendEmail import *
from ui import login, applicantDashboard, managerDashboard, managerApplicantLog, managerTeamMembers, \
    managerMemberProfile, managerAddNewMember, managerEditMemberProfile, adminManagerProfiles, adminRegisterManager, \
    managerDLeaderInfoBank, managerAddNewDLeader, managerDLeaderProfile, managerEditDLeaderProfile


def verifyUsername(username):
    userPattern = r"^[a-zA-Z][a-zA-Z0-9_]*$"
    return re.match(userPattern, username)


class loginWindow(login.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        # applicant
        self.btn_applicantLogin.clicked.connect(self.loginApplicant)
        self.btn_applicantCancel.clicked.connect(self.cancel)
        self.check_applicantShowPass.clicked.connect(self.showPass)

        # manager
        self.btn_managerLogin.clicked.connect(self.loginManager)
        self.btn_managerCancel.clicked.connect(self.cancel)
        self.check_managerShowPass.clicked.connect(self.showPass)

        # line edits
        # applicant
        self.line_applicantUsername.textChanged.connect(self.printApplicantUsername)
        self.line_applicantUsername.returnPressed.connect(self.enterPressed)
        self.line_applicantPassword.textChanged.connect(self.printPassword)
        self.line_applicantPassword.returnPressed.connect(self.loginApplicant)

        # manager
        self.line_managerUsername.textChanged.connect(self.printManagerUsername)
        self.line_managerUsername.returnPressed.connect(self.enterPressed)
        self.line_managerPassword.textChanged.connect(self.printPassword)
        self.line_managerPassword.returnPressed.connect(self.loginManager)

    def printApplicantUsername(self):
        usernameEntered = self.line_applicantUsername.text()
        filteredUser = verifyUsername(usernameEntered)
        if filteredUser:
            self.line_applicantUsername.setText(filteredUser.group())
        else:
            cursor = self.line_applicantUsername.cursorPosition()
            self.line_applicantUsername.setText(usernameEntered[:cursor - 1] + usernameEntered[cursor:])
            self.line_applicantUsername.setCursorPosition(cursor - 1)

    def printManagerUsername(self):
        usernameEntered = self.line_managerUsername.text()
        filteredUser = verifyUsername(usernameEntered)
        if filteredUser:
            self.line_managerUsername.setText(filteredUser.group())
        else:
            cursor = self.line_managerUsername.cursorPosition()
            self.line_managerUsername.setText(usernameEntered[:cursor - 1] + usernameEntered[cursor:])
            self.line_managerUsername.setCursorPosition(cursor - 1)

    def printPassword(self):
        self.line_applicantPassword.setText(self.line_applicantPassword.text())
        self.line_managerPassword.setText(self.line_managerPassword.text())

    def enterPressed(self):
        self.line_applicantPassword.setFocus()
        self.line_managerPassword.setFocus()

    def loginApplicant(self):
        loginType = 'applicant'
        usernameEntered = self.line_applicantUsername.text()
        passwordEntered = self.line_applicantPassword.text()
        if general.verifyLogin(usernameEntered, passwordEntered, loginType):
            messageBox('Success', 'Logged in Successfully!', 'information')
            print('Login Successfully!')

            # change UI details in applicant dashboard
            result = applicants.fetchApplicantDetails(usernameEntered)
            if result:
                applicantName, applicantID, dleaderName, applicantMobileNumber, applicantEmail, applicantDOB = result

            applicantDashboardWindow.label_applicantName.setText(f'{applicantName}')
            applicantDashboardWindow.label_applicantID.setText(f'Applicant ID: {applicantID}')
            applicantDashboardWindow.label_dLeader.setText(f'Discipleship Leader: {dleaderName}')
            applicantDashboardWindow.label_mobileNumber.setText(f'Mobile Number: {applicantMobileNumber}')
            applicantDashboardWindow.label_emailAddress.setText(f'Email Address: {applicantEmail}')
            applicantDashboardWindow.label_dob.setText(f'Date of Birth: {applicantDOB}')

            self.close()
            applicantDashboardWindow.show()
            self.line_applicantPassword.clear()
        else:
            messageBox('Error', 'Invalid username or password! Please try again.', 'warning')
            self.line_applicantPassword.setFocus()

    def loginManager(self):
        loginType = 'manager'
        usernameEntered = self.line_managerUsername.text()
        passwordEntered = self.line_managerPassword.text()
        if general.verifyLogin(usernameEntered, passwordEntered, loginType):
            messageBox('Success', 'Logged in Successfully!', 'information')
            print('Login Successfully!')

            # change UI details in manager dashboard
            currentTime = QDateTime.currentDateTime().time()
            managerName = managers.fetchManagerDetails(usernameEntered)

            permissionLevel = managers.getPermissionLevel(usernameEntered)

            if permissionLevel == 1:
                managerDashboardWindow.label_adminDashboard.setVisible(False)
                managerDashboardWindow.btn_adminAudits.setVisible(False)
                managerDashboardWindow.btn_adminManagerProfile.setVisible(False)
            elif permissionLevel == 2:
                managerDashboardWindow.label_adminDashboard.setVisible(True)
                managerDashboardWindow.btn_adminAudits.setVisible(True)
                managerDashboardWindow.btn_adminManagerProfile.setVisible(True)

            if currentTime < QDateTime.currentDateTime().time().fromString("12:00", "hh:mm"):
                morning = [f"⛅ Sun's up! Good morning, {managerName}!",
                           f"🏆 New day. New wins! You got this, {managerName}!",
                           f"☕ Rise and shine, it's coffee time! Good morning, {managerName}!",
                           f"🌤️ Sunshine is the best medicine. Good morning, {managerName}!",
                           f"🥇 Excellence awaits. Good morning, {managerName}!"]
                message = random.choice(morning)
            elif currentTime < QDateTime.currentDateTime().time().fromString("17:00", "hh:mm"):
                afternoon = [f"🌟 The half of the day is over, but there's time to make it amazing!",
                             f"🚫 No yawns allowed in the afternoon zone. Stay alert, {managerName}!",
                             f"☕️ A cup of coffee and a smile is all you need. Good afternoon, {managerName}!",
                             f"🚀 Stay sharp, {managerName}!",
                             f"🏴 Halfway there! No slowing down, {managerName}!"]
                message = random.choice(afternoon)
            else:
                evening = [f"✨ Under the stars! Good evening, {managerName}!",
                           f"🌌 Evening breeze, good vibes! Enjoy your night, {managerName}!",
                           f"😌 Evening: the perfect time to relax and unwind.",
                           f"🌆 Good evening, {managerName}! What's your next adventure?",
                           f"🌙 Peaceful mode: on. Enjoy your evening, {managerName}!"]
                message = random.choice(evening)
            managerDashboardWindow.label_greeting.setText(f'{message}')

            self.close()
            managerDashboardWindow.show()
            self.line_managerPassword.clear()
        else:
            messageBox('Error', 'Invalid username or password! Please try again.', 'warning')
            self.line_managerPassword.setFocus()

    def showPass(self):
        if self.check_applicantShowPass.isChecked():
            self.line_applicantPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        elif not self.check_applicantShowPass.isChecked():
            self.line_applicantPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        if self.check_managerShowPass.isChecked():
            self.line_managerPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        elif not self.check_managerShowPass.isChecked():
            self.line_managerPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
        else:
            self.line_applicantPassword.setFocus()
            self.line_managerPassword.setFocus()


class applicantDashboardWindow(applicantDashboard.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_prevApplications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.previousApplications()

        # slots and signals

        # buttons
        self.btn_logout.clicked.connect(self.logout)
        # self.btn_newApplication.clicked.connect(self.newApplication)

    def previousApplications(self):
        header = ['Application ID', 'Date', 'Team', 'Status']
        data = applicants.getPreviousApplications()
        self.previousApplicationsTable = tableModel(self, data, header)

        self.tbl_prevApplications.setModel(self.previousApplicationsTable)
        self.tbl_prevApplications.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.tbl_prevApplications.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tbl_prevApplications.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tbl_prevApplications.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def logout(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class managerDashboardWindow(managerDashboard.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_pendingApplications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # slots and signals

        # buttons
        self.btn_applicantLog.clicked.connect(self.applicantLog)
        self.btn_teamMembers.clicked.connect(self.teamMembers)
        self.btn_dLeaderInfoBank.clicked.connect(self.dLeaderInfoBank)
        self.btn_adminManagerProfile.clicked.connect(self.adminManagerProfiles)
        self.btn_logout.clicked.connect(self.logout)

        # tables
        self.chart_memberStats = QChartView(self.chart_memberStats)
        self.chart_memberStats.setGeometry(self.chart_memberStats.rect())
        self.chart_memberStats.resize(406, 249)

        # show tables
        self.showMemberStats()
        self.pendingApplications()

    def applicantLog(self):
        managerApplicantLogWindow.show()
        managerApplicantLogWindow.setFocus()

    def teamMembers(self):
        managerTeamMembersWindow.show()
        managerTeamMembersWindow.setFocus()

    def dLeaderInfoBank(self):
        managerDLeaderInfoBankWindow.show()
        managerDLeaderInfoBankWindow.setFocus()

    def adminManagerProfiles(self):
        adminManagerProfilesWindow.show()
        adminManagerProfilesWindow.setFocus()

    def pendingApplications(self, keyword=None):
        header = ['Application ID', 'Applicant Name', 'Date of Application', 'Team']
        data = managers.getPendingApplications(keyword)

        if not data:
            data = ['', '', '', '']

        self.pendingApplicationsTable = tableModel(self, data, header)
        self.tbl_pendingApplications.setModel(self.pendingApplicationsTable)
        self.tbl_pendingApplications.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.tbl_pendingApplications.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tbl_pendingApplications.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def showMemberStats(self):
        teams, memberCounts = managers.getMemberStats()

        barSeries = QBarSeries()

        set1 = QBarSet('Member Count')
        set1.append(memberCounts)
        barSeries.append(set1)

        chart = QChart()
        chart.addSeries(barSeries)

        chart.setTitle('Member Statistics')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = [str(team) for team in teams]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        axisX.setLabelsAngle(45)  # rotates labels 45 degrees
        chart.addAxis(axisX, QtCore.Qt.AlignBottom)
        barSeries.attachAxis(axisX)

        self.chart_memberStats.setChart(chart)
        self.chart_memberStats.setRenderHint(QtGui.QPainter.Antialiasing)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        self.chart_memberStats.show()

    def logout(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class managerApplicantLogWindow(managerApplicantLog.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_applicantLog.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.applicantLog()

        # slots and signals

        # buttons
        self.btn_delApplicant.clicked.connect(self.deleteApplicant)
        self.btn_backToDashboard.clicked.connect(self.backToDashboard)

        # line edits
        self.line_searchBar.textChanged.connect(self.applicantLog)

    def applicantLog(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Applicant ID', 'Applicant Name', 'Mobile Number', 'Team']
        data = managers.getApplicants(keyword)

        if not data:
            data = ['', '', '', '']

        self.pendingApplicationsTable = tableModel(self, data, header)
        self.tbl_applicantLog.setModel(self.pendingApplicationsTable)
        self.tbl_applicantLog.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.tbl_applicantLog.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tbl_applicantLog.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def deleteApplicant(self):
        selectedApplicantIndex = self.tbl_applicantLog.selectionModel().currentIndex()

        if selectedApplicantIndex.isValid():
            applicationID = self.pendingApplicationsTable.data(
                self.pendingApplicationsTable.index(selectedApplicantIndex.row(), 0), QtCore.Qt.DisplayRole)
            applicantName = self.pendingApplicationsTable.data(
                self.pendingApplicationsTable.index(selectedApplicantIndex.row(), 1), QtCore.Qt.DisplayRole)
            if messageBox('Confirmation', f'Are you sure you want to delete [{applicantName}]? \n'
                                          f'This action cannot be undone.', 'question',
                          True) == QtWidgets.QMessageBox.Ok:
                managers.removeApplicant(applicationID)
                messageBox('Success', f'{applicantName} has been removed.', 'information')

                managerApplicantLogWindow.applicantLog()
                managerDashboardWindow.pendingApplications()
            else:
                self.setFocus()

    def backToDashboard(self):
        self.close()
        managerDashboardWindow.setFocus()


class managerTeamMembersWindow(managerTeamMembers.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_teamMembers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.teamMembers()

        # slots and signals

        # buttons
        self.btn_backToDashboard.clicked.connect(self.backToDashboard)
        self.combo_teamSelect.currentIndexChanged.connect(self.applyFilters)
        self.btn_addNewMember.clicked.connect(self.managerAddNewMember)
        self.btn_deleteMember.clicked.connect(self.managerDeleteMember)

        # line edits
        self.line_searchBar.textChanged.connect(self.teamMembers)

        # row click
        self.tbl_teamMembers.doubleClicked.connect(self.viewMemberProfile)

    def teamMembers(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Member ID', 'Member Name', 'Team']
        data = managers.getTeamMembers(keyword)

        if not data:
            data = ['', '', '']

        self.teamMembersTable = tableModel(self, data, header)
        self.tbl_teamMembers.setModel(self.teamMembersTable)
        self.tbl_teamMembers.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.tbl_teamMembers.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tbl_teamMembers.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def applyFilters(self):
        teamFilter = self.combo_teamSelect.currentText()
        self.teamMembersTable.setTeamFilters(teamFilter)

    def managerAddNewMember(self):
        managerAddNewMemberWindow.show()
        managerAddNewMemberWindow.setFocus()

    def managerDeleteMember(self):
        selectedMemberIndex = self.tbl_teamMembers.selectionModel().currentIndex()

        if selectedMemberIndex.isValid():
            memberID = self.teamMembersTable.data(
                self.teamMembersTable.index(selectedMemberIndex.row(), 0), QtCore.Qt.DisplayRole)
            memberName = self.teamMembersTable.data(
                self.teamMembersTable.index(selectedMemberIndex.row(), 1), QtCore.Qt.DisplayRole)
            print(memberID)
            if messageBox('Confirmation', f'Are you sure you want to delete [{memberName}]? \n'
                                          f'This action cannot be undone.', 'question',
                          True) == QtWidgets.QMessageBox.Ok:
                managers.removeMember(memberID)
                messageBox('Success', f'{memberName} has been removed.', 'information')

                self.teamMembers()
                managerDashboardWindow.showMemberStats()
            else:
                self.setFocus()

    def viewMemberProfile(self):
        selectedMemberIndex = self.tbl_teamMembers.selectionModel().currentIndex()

        if selectedMemberIndex.isValid():
            member = self.teamMembersTable.data(
                self.teamMembersTable.index(selectedMemberIndex.row(), 0), QtCore.Qt.DisplayRole)
            print(member)

            # change UI details in manager member profile
            result = managers.fetchMemberDetails(member)
            if result:
                memberName, memberID, teamName, memberDOB, memberAge, memberMobileNumber, memberEmail, dleaderName = result

            managerMemberProfileWindow.label_memberName.setText(f'{memberName}')
            managerMemberProfileWindow.label_memberID_filler.setText(f'{memberID}')
            managerMemberProfileWindow.label_team_filler.setText(f'{teamName}')
            managerMemberProfileWindow.label_dob_filler.setText(f'{memberDOB}')
            managerMemberProfileWindow.label_age_filler.setText(f'{memberAge}')
            managerMemberProfileWindow.label_mobileNumber_filler.setText(f'{memberMobileNumber}')
            managerMemberProfileWindow.label_email_filler.setText(f'{memberEmail}')
            managerMemberProfileWindow.label_dLeader_filler.setText(f'{dleaderName}')

            managerMemberProfileWindow.setWindowTitle(f'{memberName}')

            managerMemberProfileWindow.show()

    def backToDashboard(self):
        managerDashboardWindow.show()
        self.close()
        managerDashboardWindow.setFocus()


class managerMemberProfileWindow(managerMemberProfile.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        self.btn_editProfile.clicked.connect(self.editProfile)
        self.btn_close.clicked.connect(self.backToDashboard)

    def editProfile(self):
        memberID = self.label_memberID_filler.text()

        # change UI details in manager edit member profile
        result = managers.fetchMemberDetails(memberID)
        if result:
            memberName, memberID, teamName, memberDOB, memberAge, memberMobileNumber, memberEmail, dleaderName = result

        if teamName == 'Camera & Graphics':
            teamIndex = 1
        elif teamName == 'Sounds & Lights':
            teamIndex = 2
        elif teamName == 'Stage Management':
            teamIndex = 3
        else:
            teamIndex = 0

        managerEditMemberProfileWindow.label_memberName.setText(f'{memberName}')
        managerEditMemberProfileWindow.label_memberID_filler.setText(f'{memberID}')
        managerEditMemberProfileWindow.combo_teamSelect.setCurrentIndex(teamIndex)
        # dleader
        managerEditMemberProfileWindow.line_mobileNumber.setPlaceholderText(f'{memberMobileNumber}')
        managerEditMemberProfileWindow.date_dob.setDate(memberDOB)
        managerEditMemberProfileWindow.label_age_filler.setText(f'{memberAge}')
        managerEditMemberProfileWindow.line_email.setPlaceholderText(f'{memberEmail}')

        managerEditMemberProfileWindow.setWindowTitle(f'Editing {memberName}')

        managerEditMemberProfileWindow.show()
        managerMemberProfileWindow.setFocus()

    def backToDashboard(self):
        managerTeamMembersWindow.show()
        self.close()
        managerTeamMembersWindow.setFocus()


class managerEditMemberProfileWindow(managerEditMemberProfile.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # text edits
        self.line_mobileNumber.textChanged.connect(self.printMobileNumber)
        self.line_email.textChanged.connect(self.printEmail)

        # buttons
        self.btn_saveChanges.clicked.connect(self.saveChanges)
        self.btn_cancel.clicked.connect(self.cancel)

        # date entry
        self.date_dob.setCalendarPopup(True)
        self.date_dob.dateChanged.connect(self.printDob)

        # validators
        self.line_mobileNumber.setValidator(QtGui.QIntValidator())

    def printMobileNumber(self):
        self.line_mobileNumber.setText(self.line_mobileNumber.text())

    def printEmail(self):
        self.line_email.setText(self.line_email.text())

    def printDLeader(self):
        dLeader = self.combo_dLeader.currentText()
        self.combo_dLeader.setCurrentText(dLeader)

    def teamSelect(self):
        team = self.combo_teamSelect.currentText()
        self.combo_teamSelect.setCurrentText(team)

    def printDob(self):
        self.date_dob.setDate(self.date_dob.date())

    def saveChanges(self):
        member = self.label_memberID_filler.text()

        team = self.combo_teamSelect.currentText()
        dleaderIndex = self.combo_dLeader.currentText()
        dob = self.date_dob.text()
        mobileNumber = self.line_mobileNumber.text()
        email = self.line_email.text()

        if team != 'Select Option':
            if team == 'Camera & Graphics':
                teamIndex = '1'
            elif team == 'Sounds & Lights':
                teamIndex = '2'
            elif team == 'Stage Management':
                teamIndex = '3'
        else:
            teamIndex = None

        if dleaderIndex == '':
            dleaderIndex = None

        if email == '':
            email = None

        if messageBox('Confirmation', 'Are you sure you want to save changes?', 'question',
                      True) == QtWidgets.QMessageBox.Ok:
            managers.editMemberProfile(teamIndex, dleaderIndex, dob, mobileNumber, email, member)
            messageBox('Success!', 'Changes saved successfully!', 'information', False)

            managerTeamMembersWindow.teamMembers()

            self.line_mobileNumber.clear()
            self.line_email.clear()
            self.close()
        else:
            self.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            managerMemberProfileWindow.show()
            self.close()
            managerMemberProfileWindow.setFocus()
        else:
            self.setFocus()


class managerAddNewMemberWindow(managerAddNewMember.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        self.btn_addNewMember.clicked.connect(self.addMember)
        self.btn_cancel.clicked.connect(self.cancel)
        self.combo_teamSelect.currentIndexChanged.connect(self.teamSelect)
        self.combo_dLeader.currentIndexChanged.connect(self.printDLeader)

        # line edits
        self.line_firstName.textChanged.connect(self.printFirstName)
        self.line_surname.textChanged.connect(self.printSurname)
        self.line_mobileNumber.textChanged.connect(self.printMobileNumber)
        self.line_email.textChanged.connect(self.printEmail)

        # date entry
        self.date_dob.setCalendarPopup(True)
        self.date_dob.dateChanged.connect(self.printDob)

        # validators
        self.line_mobileNumber.setValidator(QtGui.QIntValidator())

    def printFirstName(self):
        self.line_firstName.setText(self.line_firstName.text())

    def printSurname(self):
        self.line_surname.setText(self.line_surname.text())

    def printMobileNumber(self):
        self.line_mobileNumber.setText(self.line_mobileNumber.text())

    def printEmail(self):
        self.line_email.setText(self.line_email.text())

    def printDLeader(self):
        dLeader = self.combo_dLeader.currentText()
        self.combo_dLeader.setCurrentText(dLeader)

    def teamSelect(self):
        team = self.combo_teamSelect.currentText()
        self.combo_teamSelect.setCurrentText(team)

    def printDob(self):
        self.date_dob.setDate(self.date_dob.date())

    def addMember(self):
        firstName = self.line_firstName.text()
        surname = self.line_surname.text()
        dob = self.date_dob.text()
        mobileNumber = self.line_mobileNumber.text()
        team = self.combo_teamSelect.currentText()
        email = self.line_email.text()
        dleaderIndex = self.combo_dLeader.currentText()

        if team != 'Select Option':
            if team == 'Camera & Graphics':
                teamIndex = '1'
            elif team == 'Sounds & Lights':
                teamIndex = '2'
            elif team == 'Stage Management':
                teamIndex = '3'
        else:
            teamIndex = ''

        if email == '':
            email = None

        if dleaderIndex == '':
            dleaderIndex = None

        if firstName and surname and dob and mobileNumber and teamIndex != '':
            checkDuplicateName = managers.getTeamMembers(firstName + surname)

            if checkDuplicateName:
                messageBox('Error', 'Member already exists!', 'critical', False)
                self.setFocus()
            elif messageBox('Confirmation', 'Are you sure you want to register this member?', 'question', True) == \
                    QtWidgets.QMessageBox.Ok:
                managers.addNewMember(firstName, surname, dob, mobileNumber, teamIndex, email, dleaderIndex)
                messageBox('Success', 'Member successfully registered!', 'information', False)

                managerTeamMembersWindow.show()
                managerTeamMembersWindow.teamMembers()
                managerDashboardWindow.showMemberStats()
                self.close()
                managerTeamMembersWindow.setFocus()
            else:
                self.setFocus()
        else:
            messageBox('Error', 'Please fill in all the fields!', 'critical', False)
            self.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            managerTeamMembersWindow.show()
            self.close()
            managerTeamMembersWindow.setFocus()
        else:
            self.setFocus()


class managerDLeaderInfoBankWindow(managerDLeaderInfoBank.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_dLeaderTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # slots and signals

        # buttons
        self.btn_addNewDLeader.clicked.connect(self.addNewDLeader)
        self.btn_removeDLeader.clicked.connect(self.removeDLeader)
        self.btn_backToDashboard.clicked.connect(self.backToDashboard)

        # row click
        self.tbl_dLeaderTable.doubleClicked.connect(self.viewDLeaderProfile)

        # line edits
        self.line_searchBar.textChanged.connect(self.dLeaderInfoBank)

        self.dLeaderInfoBank()

    def dLeaderInfoBank(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['DLeader ID', 'Discipleship Leader Name']
        data = managers.getDLeaders(keyword)

        if not data:
            data = ['', '']

        self.dLeaderTable = tableModel(self, data, header)
        self.tbl_dLeaderTable.setModel(self.dLeaderTable)
        self.tbl_dLeaderTable.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.tbl_dLeaderTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def addNewDLeader(self):
        managerAddNewDLeaderWindow.show()
        managerAddNewDLeaderWindow.setFocus()

    def viewDLeaderProfile(self):
        selectedDLeaderIndex = self.tbl_dLeaderTable.selectionModel().currentIndex()

        if selectedDLeaderIndex.isValid():
            dleaderID = self.dLeaderTable.data(
                self.dLeaderTable.index(selectedDLeaderIndex.row(), 0), QtCore.Qt.DisplayRole)

            # change UI details in manager dleader profile
            result = managers.fetchDLeaderDetails(dleaderID)
            if result:
                dleaderName, dleaderID, dleaderMobileNumber, dleaderEmail = result

            managerDLeaderProfileWindow.setDLeaderDetails(dleaderID, dleaderEmail)
            managerDLeaderProfileWindow.dMembers()
            managerDLeaderProfileWindow.label_dLeaderName.setText(f'{dleaderName}')
            managerDLeaderProfileWindow.label_dLeaderID_filler.setText(f'{dleaderID}')
            managerDLeaderProfileWindow.label_mobileNumber_filler.setText(f'{dleaderMobileNumber}')
            managerDLeaderProfileWindow.label_email_filler.setText(f'{dleaderEmail}')

            managerDLeaderProfileWindow.setWindowTitle(f'{dleaderName}')

            managerDLeaderProfileWindow.show()

    def removeDLeader(self):
        selectedDLeaderIndex = self.tbl_dLeaderTable.selectionModel().currentIndex()

        if selectedDLeaderIndex.isValid():
            dleaderID = self.dLeaderTable.data(
                self.dLeaderTable.index(selectedDLeaderIndex.row(), 0), QtCore.Qt.DisplayRole)
            dleaderName = self.dLeaderTable.data(
                self.dLeaderTable.index(selectedDLeaderIndex.row(), 1), QtCore.Qt.DisplayRole)
            if messageBox('Confirmation', f'Are you sure you want to delete [{dleaderName}]? \n'
                                          f'This action cannot be undone.', 'question',
                          True) == QtWidgets.QMessageBox.Ok:
                managers.removeDLeader(dleaderID)
                messageBox('Success', f'{dleaderName} has been removed.', 'information')

                managerDLeaderInfoBankWindow.dLeaderInfoBank()
            else:
                self.setFocus()

    def backToDashboard(self):
        managerDashboardWindow.show()
        self.close()
        managerDashboardWindow.setFocus()


class managerDLeaderProfileWindow(managerDLeaderProfile.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dleaderID = None
        self.dleaderEmail = self.label_email_filler.text()

        self.tbl_dMembers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # slots and signals

        # buttons
        self.btn_editProfile.clicked.connect(self.editProfile)
        self.btn_sendEmail.clicked.connect(self.sendEmail)
        self.btn_close.clicked.connect(self.cancel)

        # line edits
        self.line_searchBar.textChanged.connect(self.dMembers)

    def setDLeaderDetails(self, dleaderID, dleaderEmail):
        self.dleaderID = dleaderID
        self.dleaderEmail = dleaderEmail

    def dMembers(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Member ID', 'Member Name', 'Team']
        data = managers.fetchDLeaderMembers(self.dleaderID, keyword)

        if not data:
            data = [['', '', '']]

        self.dMembersTable = tableModel(self, data, header)
        self.tbl_dMembers.setModel(self.dMembersTable)
        self.tbl_dMembers.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.tbl_dMembers.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tbl_dMembers.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def editProfile(self):
        # change UI details in manager edit dleader profile
        result = managers.fetchDLeaderDetails(self.dleaderID)
        if result:
            dleaderName, dleaderID, dleaderMobileNumber, dleaderEmail = result

        managerEditDLeaderProfileWindow.label_dLeaderName.setText(f'{dleaderName}')
        managerEditDLeaderProfileWindow.label_dLeaderID_filler.setText(f'{dleaderID}')
        managerEditDLeaderProfileWindow.line_mobileNumber.setPlaceholderText(f'{dleaderMobileNumber}')
        managerEditDLeaderProfileWindow.line_email.setPlaceholderText(f'{dleaderEmail}')

        managerEditDLeaderProfileWindow.setWindowTitle(f'Editing {dleaderName}')

        managerEditDLeaderProfileWindow.show()
        managerDLeaderProfileWindow.setFocus()

    def sendEmail(self):
        selectedMemberIndex = self.tbl_dMembers.selectionModel().currentIndex()
        subject = 'Request for approval'
        recipient = self.dleaderEmail

        if selectedMemberIndex.isValid():
            member = self.dMembersTable.data(
                self.dMembersTable.index(selectedMemberIndex.row(), 1), QtCore.Qt.DisplayRole)
            team = self.dMembersTable.data(
                self.dMembersTable.index(selectedMemberIndex.row(), 2), QtCore.Qt.DisplayRole)

            message = f'''
            To whom it may concern,
            
            This email has been send to request approval for {member} to join the {team} team in the Live Production ministry within CCF.
            
            Please send a reply to this email to acknowledge receipt and confirm approval.
            
            Sincerely yours,
            CCF Live Production Ministry'''

            if sendEmailMsg(recipient, subject, message):
                messageBox('Success', 'Email sent successfully!', 'information', False)
            else:
                messageBox('Error', 'Failed to send email.', 'critical', False)
        else:
            messageBox('Error', 'Please select a member.', 'critical', False)

    def cancel(self):
        managerDLeaderInfoBankWindow.show()
        self.close()
        managerDLeaderInfoBankWindow.setFocus()


class managerAddNewDLeaderWindow(managerAddNewDLeader.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        self.btn_addNewDLeader.clicked.connect(self.addDLeader)
        self.btn_cancel.clicked.connect(self.cancel)

        # line edits
        self.line_firstName.textChanged.connect(self.printFirstName)
        self.line_surname.textChanged.connect(self.printSurname)
        self.line_mobileNumber.textChanged.connect(self.printMobileNumber)
        self.line_email.textChanged.connect(self.printEmail)

        # validators
        self.line_mobileNumber.setValidator(QtGui.QIntValidator())

    def printFirstName(self):
        self.line_firstName.setText(self.line_firstName.text())

    def printSurname(self):
        self.line_surname.setText(self.line_surname.text())

    def printMobileNumber(self):
        self.line_mobileNumber.setText(self.line_mobileNumber.text())

    def printEmail(self):
        self.line_email.setText(self.line_email.text())

    def addDLeader(self):
        firstName = self.line_firstName.text()
        surname = self.line_surname.text()
        mobileNumber = self.line_mobileNumber.text()
        email = self.line_email.text()

        if firstName and surname and mobileNumber and email:
            checkDuplicateName = managers.getDLeaders(firstName + surname)

            if checkDuplicateName:
                messageBox('Error', 'DLeader already exists!', 'critical', False)
                self.setFocus()
            elif messageBox('Confirmation', 'Are you sure you want to register this DLeader?', 'question', True) == \
                    QtWidgets.QMessageBox.Ok:
                managers.addNewDLeader(firstName, surname, mobileNumber, email)
                messageBox('Success', 'DLeader successfully registered!', 'information', False)

                self.line_firstName.clear()
                self.line_surname.clear()
                self.line_mobileNumber.clear()
                self.line_email.clear()

                managerDLeaderInfoBankWindow.dLeaderInfoBank()

                managerDLeaderInfoBankWindow.show()
                self.close()
                managerDLeaderInfoBankWindow.setFocus()
            else:
                self.setFocus()
        else:
            messageBox('Error', 'Please fill in all the fields!', 'critical', False)
            self.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            managerDLeaderInfoBankWindow.show()
            self.close()
            managerDLeaderInfoBankWindow.setFocus()
        else:
            self.setFocus()


class managerEditDLeaderProfileWindow(managerEditDLeaderProfile.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # text edits
        self.line_mobileNumber.textChanged.connect(self.printMobileNumber)
        self.line_email.textChanged.connect(self.printEmail)

        # buttons
        self.btn_saveChanges.clicked.connect(self.saveChanges)
        self.btn_cancel.clicked.connect(self.cancel)

        # validators
        self.line_mobileNumber.setValidator(QtGui.QIntValidator())

    def printMobileNumber(self):
        self.line_mobileNumber.setText(self.line_mobileNumber.text())

    def printEmail(self):
        self.line_email.setText(self.line_email.text())

    def saveChanges(self):
        dleader = self.label_dLeaderID_filler.text()

        mobileNumber = self.line_mobileNumber.text()
        email = self.line_email.text()

        if email == '':
            email = None

        if messageBox('Confirmation', 'Are you sure you want to save changes?', 'question',
                      True) == QtWidgets.QMessageBox.Ok:
            managers.editDLeaderProfile(mobileNumber, email, dleader)
            messageBox('Success!', 'Changes saved successfully!', 'information', False)
            self.line_mobileNumber.clear()
            self.line_email.clear()
            self.close()
        else:
            self.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            managerDLeaderInfoBankWindow.show()
            self.close()
            managerDLeaderInfoBankWindow.setFocus()
        else:
            self.setFocus()


class adminManagerProfilesWindow(adminManagerProfiles.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_managerProfiles.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.managerProfiles()

        # slots and signals

        # buttons
        self.btn_backToDashboard.clicked.connect(self.backToDashboard)
        self.btn_registerManager.clicked.connect(self.adminRegisterManager)

        # row click
        self.btn_removeManager.clicked.connect(self.deleteManagerProfile)

        # line edits
        self.line_searchBar.textChanged.connect(self.managerProfiles)

    def managerProfiles(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Manager ID', 'Manager Name', 'Manager Username', 'Permission Level']
        data = administrators.getManagerProfiles(keyword)

        if not data:
            data = ['', '', '', '']

        self.managerProfilesTable = tableModel(self, data, header)
        self.tbl_managerProfiles.setModel(self.managerProfilesTable)
        self.tbl_managerProfiles.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.tbl_managerProfiles.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tbl_managerProfiles.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def deleteManagerProfile(self):
        selectedManagerIndex = self.tbl_managerProfiles.selectionModel().currentIndex()

        if selectedManagerIndex.isValid():
            managerID = self.managerProfilesTable.data(
                self.managerProfilesTable.index(selectedManagerIndex.row(), 0), QtCore.Qt.DisplayRole)
            managerName = self.managerProfilesTable.data(
                self.managerProfilesTable.index(selectedManagerIndex.row(), 1), QtCore.Qt.DisplayRole)
            if messageBox('Confirmation', f'Are you sure you want to delete [{managerName}]? \n'
                                          f'This action cannot be undone.', 'question',
                          True) == QtWidgets.QMessageBox.Ok:
                administrators.removeManager(managerID)
                messageBox('Success', f'{managerName} has been removed.', 'information')

                adminManagerProfilesWindow.managerProfiles()
            else:
                self.setFocus()

    def adminRegisterManager(self):
        adminRegisterManagerWindow.show()
        adminRegisterManagerWindow.setFocus()

    def backToDashboard(self):
        managerDashboardWindow.show()
        self.close()
        managerDashboardWindow.setFocus()


class adminRegisterManagerWindow(adminRegisterManager.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        self.btn_registerManager.clicked.connect(self.registerManager)
        self.btn_cancel.clicked.connect(self.cancel)

        # text edits
        self.line_firstName.textChanged.connect(self.printFirstName)
        self.line_surname.textChanged.connect(self.printSurname)
        self.line_username.textChanged.connect(self.printUsername)
        self.line_password.textChanged.connect(self.printPassword)

    def printFirstName(self):
        self.line_firstName.setText(self.line_firstName.text())

    def printSurname(self):
        self.line_surname.setText(self.line_surname.text())

    def printUsername(self):
        usernameEntered = self.line_username.text()
        filteredUser = verifyUsername(usernameEntered)
        if filteredUser:
            self.line_username.setText(filteredUser.group())
        else:
            cursor = self.line_username.cursorPosition()
            self.line_username.setText(usernameEntered[:cursor - 1] + usernameEntered[cursor:])
            self.line_username.setCursorPosition(cursor - 1)

    def printPassword(self):
        self.line_password.setText(self.line_password.text())

    def registerManager(self):
        firstName = self.line_firstName.text()
        surname = self.line_surname.text()
        username = self.line_username.text()
        password = self.line_password.text()
        permission = self.combo_permission.currentText()

        if permission != 'Select Option':
            if permission == 'Manager':
                permissionLevel = '1'
            if permission == 'Administrator':
                permissionLevel = '2'
        else:
            permissionLevel = ''

        if firstName and surname and username and password and permissionLevel:
            checkDuplicateName = administrators.getManagerProfiles(firstName + surname)
            checkDuplicateUsername = administrators.getManagerProfiles(username)

            if checkDuplicateName or checkDuplicateUsername:
                messageBox('Error', 'Manager already exists!', 'critical', False)
                self.setFocus()
            elif messageBox('Confirmation', 'Are you sure you want to register this manager?', 'question', True) == \
                    QtWidgets.QMessageBox.Ok:
                administrators.add(firstName, surname, username, password, permissionLevel)
                messageBox('Success', 'Manager successfully registered!', 'information', False)

                self.line_firstName.clear()
                self.line_surname.clear()
                self.line_username.clear()
                self.line_password.clear()

                adminManagerProfilesWindow.managerProfiles()

                adminManagerProfilesWindow.show()
                self.close()
                adminManagerProfilesWindow.setFocus()
            else:
                self.setFocus()
        else:
            messageBox('Error', 'Please fill in all the fields!', 'critical', False)
            self.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            adminManagerProfilesWindow.show()
            self.close()
            adminManagerProfilesWindow.setFocus()
        else:
            self.setFocus()


if __name__ == '__main__':
    Database.initialize(database='ccf-volunteers', user='postgres', password='543738', host='localhost', port='5432')

    app = QApplication(sys.argv)

    loginWindow = loginWindow()
    applicantDashboardWindow = applicantDashboardWindow()
    managerDashboardWindow = managerDashboardWindow()
    managerApplicantLogWindow = managerApplicantLogWindow()
    managerTeamMembersWindow = managerTeamMembersWindow()
    managerAddNewMemberWindow = managerAddNewMemberWindow()
    managerMemberProfileWindow = managerMemberProfileWindow()
    managerEditMemberProfileWindow = managerEditMemberProfileWindow()
    managerDLeaderInfoBankWindow = managerDLeaderInfoBankWindow()
    managerAddNewDLeaderWindow = managerAddNewDLeaderWindow()
    managerDLeaderProfileWindow = managerDLeaderProfileWindow()
    managerEditDLeaderProfileWindow = managerEditDLeaderProfileWindow()
    adminManagerProfilesWindow = adminManagerProfilesWindow()
    adminRegisterManagerWindow = adminRegisterManagerWindow()

    loginWindow.show()
    sys.exit(app.exec_())
