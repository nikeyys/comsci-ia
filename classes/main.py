import logging
import random
import re  # regex
import sys
from datetime import timedelta

from PyQt5.QtChart import QChart, QBarSeries, QBarSet, QBarCategoryAxis, QChartView
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication

from classes.dialogBoxes import *
from classes.object import *
from classes.sendEmail import *
from classes.tableModel import *
from ui import (login, applicantDashboard, applicantNewApplication, applicantAnotherApplication, applicantNewAccount,
                managerDashboard, managerApplicationView, managerApplicantLog, managerTeamMembers, managerMemberProfile,
                managerAddNewMember, managerEditMemberProfile, adminManagerProfiles, adminRegisterManager,
                managerDLeaderInfoBank, managerAddNewDLeader, managerDLeaderProfile, managerEditDLeaderProfile,
                adminUpdateLog)


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
        self.cmdLink_applicantCTA.clicked.connect(self.newApplication)

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

            applicantDashboardWindow.lbl_applicantName.setText(f'{applicantName}')
            applicantDashboardWindow.lbl_applicantID_filler.setText(f'{applicantID}')
            applicantDashboardWindow.lbl_dleader_filler.setText(f'{dleaderName}')
            applicantDashboardWindow.lbl_mobileNumber_filler.setText(f'{applicantMobileNumber}')
            applicantDashboardWindow.lbl_email_filler.setText(f'{applicantEmail}')
            applicantDashboardWindow.lbl_dob_filler.setText(f'{applicantDOB}')

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

    def newApplication(self):
        applicantNewApplicationWindow.show()
        applicantNewApplicationWindow.setFocus()

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
        self.btn_newApplication.clicked.connect(self.newApplication)

    def previousApplications(self):
        applicantID = self.lbl_applicantID_filler.text()

        header = ['Application ID', 'Date', 'Team', 'Status']
        data = applicants.getPreviousApplications()
        self.previousApplicationsTable = tableModel(self, data, header)

        self.tbl_prevApplications.setModel(self.previousApplicationsTable)
        self.tbl_prevApplications.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.tbl_prevApplications.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tbl_prevApplications.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tbl_prevApplications.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def newApplication(self):
        applicantID = self.lbl_applicantID_filler.text()

        applicantAnotherApplicationWindow.getApplicantID(applicantID)
        applicantAnotherApplicationWindow.show()
        applicantAnotherApplicationWindow.setFocus()

    def logout(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class applicantNewApplicationWindow(applicantNewApplication.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.responseWhenJesusLord = None
        self.responseHowJesusLord = None
        self.responseLoseSalvation = None
        self.responseMinistryToSalvation = None

        # slots and signals

        # buttons
        self.btn_submit.clicked.connect(self.submitApplication)
        self.btn_cancel.clicked.connect(self.cancel)
        self.combo_teamSelect.currentIndexChanged.connect(self.teamSelect)
        self.combo_dleader.currentIndexChanged.connect(self.printDLeader)

        # line edits
        self.line_firstName.textChanged.connect(self.printFirstName)
        self.line_surname.textChanged.connect(self.printSurname)
        self.line_mobileNumber.textChanged.connect(self.printMobileNumber)
        self.line_email.textChanged.connect(self.printEmail)
        self.line_occupation.textChanged.connect(self.printOccupation)
        self.line_employer.textChanged.connect(self.printEmployer)

        # text edits
        self.text_whenJesusLord.textChanged.connect(self.printWhenJesusLord)
        self.text_howJesusLord.textChanged.connect(self.printHowJesusLord)
        self.text_loseSalvation.textChanged.connect(self.printLoseSalvation)
        self.text_ministryToSalvation.textChanged.connect(self.printMinistryToSalvation)

        # date entry
        self.date_dob.setCalendarPopup(True)
        self.date_dob.dateChanged.connect(self.printDob)

        # validators
        self.line_mobileNumber.setValidator(QtGui.QIntValidator())

    def teamSelect(self):
        team = self.combo_teamSelect.currentText()
        self.combo_teamSelect.setCurrentText(team)

    def printDLeader(self):
        dLeader = self.combo_dleader.currentText()
        self.combo_dleader.setCurrentText(dLeader)

    def printFirstName(self):
        self.line_firstName.setText(self.line_firstName.text())

    def printSurname(self):
        self.line_surname.setText(self.line_surname.text())

    def printMobileNumber(self):
        self.line_mobileNumber.setText(self.line_mobileNumber.text())

    def printEmail(self):
        self.line_email.setText(self.line_email.text())

    def printOccupation(self):
        self.line_occupation.setText(self.line_occupation.text())

    def printEmployer(self):
        self.line_employer.setText(self.line_employer.text())

    def printWhenJesusLord(self):
        self.responseWhenJesusLord = self.text_whenJesusLord.toPlainText()

    def printHowJesusLord(self):
        self.responseHowJesusLord = self.text_howJesusLord.toPlainText()

    def printLoseSalvation(self):
        self.responseLoseSalvation = self.text_loseSalvation.toPlainText()

    def printMinistryToSalvation(self):
        self.responseMinistryToSalvation = self.text_ministryToSalvation.toPlainText()

    def printDob(self):
        self.date_dob.setDate(self.date_dob.date())

    def submitApplication(self):
        firstName = self.line_firstName.text()
        surname = self.line_surname.text()
        dob = self.date_dob.text()
        mobileNumber = self.line_mobileNumber.text()
        email = self.line_email.text()
        team = self.combo_teamSelect.currentText()
        dleader = self.combo_dleader.currentText()
        occupation = self.line_occupation.text()
        employer = self.line_employer.text()

        responseWhenJesusLord = self.responseWhenJesusLord
        responseHowJesusLord = self.responseHowJesusLord
        responseLoseSalvation = self.responseLoseSalvation
        responseMinistryToSalvation = self.responseMinistryToSalvation

        applicationDate = QDateTime.currentDateTime().date().toString("yyyy-MM-dd")

        if team == 'Camera & Graphics':
            teamIndex = 1
        elif team == 'Sounds & Lights':
            teamIndex = 2
        elif team == 'Stage Management':
            teamIndex = 3

        if email == '':
            email = None

        if dleader == '':
            dleader = None

        duplicateCheck = applicants.getApplicants(firstName + surname)
        if duplicateCheck is True:
            messageBox('Error', 'Applicant already exists!', 'critical', False)
        else:
            if (firstName and surname and mobileNumber and email and dob and responseWhenJesusLord and
                    responseHowJesusLord and responseLoseSalvation and responseMinistryToSalvation) != '':
                applicantID = applicants.addNewApplicantProfile(firstName, surname, mobileNumber, email, dob, dleader,
                                                                occupation, employer)
                applicants.addNewApplication(responseWhenJesusLord, responseHowJesusLord, responseLoseSalvation,
                                             responseMinistryToSalvation, applicationDate, applicantID, teamIndex)
                messageBox('Success', 'Application submitted successfully!', 'information', False)

                updateDetails = f'NEW APPLICATION SUBMITTED. | Application ID: {applicantID} - Team: {team}'
                adminUpdateLogWindow.logUpdate(updateDetails)
                adminUpdateLogWindow.showUpdates()
                managerDashboardWindow.showUpdates()

                applicantNewAccountWindow.getApplicantID(applicantID)
                self.close()
                applicantNewAccountWindow.show()
                applicantDashboardWindow.setFocus()
            else:
                messageBox('Error', 'Please fill in all the fields!', 'critical', False)
                self.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you wish to cancel your application? \n'
                                      'Data will not be saved.',
                      'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class applicantAnotherApplicationWindow(applicantAnotherApplication.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.applicantID = None

        self.responseWhenJesusLord = None
        self.responseHowJesusLord = None
        self.responseLoseSalvation = None
        self.responseMinistryToSalvation = None

        # slots and signals

        # buttons
        self.btn_submit.clicked.connect(self.submitApplication)
        self.btn_cancel.clicked.connect(self.cancel)
        self.combo_teamSelect.currentIndexChanged.connect(self.teamSelect)
        self.combo_dleader.currentIndexChanged.connect(self.printDLeader)

        # text edits
        self.text_whenJesusLord.textChanged.connect(self.printWhenJesusLord)
        self.text_howJesusLord.textChanged.connect(self.printHowJesusLord)
        self.text_loseSalvation.textChanged.connect(self.printLoseSalvation)
        self.text_ministryToSalvation.textChanged.connect(self.printMinistryToSalvation)

    def getApplicantID(self, applicantID):
        self.applicantID = applicantID

    def teamSelect(self):
        team = self.combo_teamSelect.currentText()
        self.combo_teamSelect.setCurrentText(team)

    def printDLeader(self):
        dLeader = self.combo_dleader.currentText()
        self.combo_dleader.setCurrentText(dLeader)

    def printWhenJesusLord(self):
        self.responseWhenJesusLord = self.text_whenJesusLord.toPlainText()

    def printHowJesusLord(self):
        self.responseHowJesusLord = self.text_howJesusLord.toPlainText()

    def printLoseSalvation(self):
        self.responseLoseSalvation = self.text_loseSalvation.toPlainText()

    def printMinistryToSalvation(self):
        self.responseMinistryToSalvation = self.text_ministryToSalvation.toPlainText()

    def submitApplication(self):
        applicantID = self.applicantID
        team = self.combo_teamSelect.currentText()

        if team == 'Camera & Graphics':
            teamIndex = 1
        elif team == 'Sounds & Lights':
            teamIndex = 2
        elif team == 'Stage Management':
            teamIndex = 3

        responseWhenJesusLord = self.responseWhenJesusLord
        responseHowJesusLord = self.responseHowJesusLord
        responseLoseSalvation = self.responseLoseSalvation
        responseMinistryToSalvation = self.responseMinistryToSalvation

        applicationDate = QDateTime.currentDateTime().date().toString("yyyy-MM-dd")
        if (responseWhenJesusLord and responseHowJesusLord and responseLoseSalvation and
                responseMinistryToSalvation) != '':
            applicants.addNewApplication(responseWhenJesusLord, responseHowJesusLord, responseLoseSalvation,
                                         responseMinistryToSalvation, applicationDate, applicantID, teamIndex)
            messageBox('Success', 'Application submitted successfully!', 'information', False)

            updateDetails = f'NEW APPLICATION SUBMITTED. | Application ID: {applicantID} - Team: {team}'
            adminUpdateLogWindow.logUpdate(updateDetails)
            adminUpdateLogWindow.showUpdates()
            managerDashboardWindow.showUpdates()

            self.close()
            applicantDashboardWindow.previousApplications()
            applicantDashboardWindow.show()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you wish to cancel your application? \n'
                                      'Data will not be saved.',
                      'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class applicantNewAccountWindow(applicantNewAccount.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.applicantID = None

        # slots and signals
        # buttons
        self.btn_createAcc.clicked.connect(self.createAccount)
        self.check_showPass.clicked.connect(self.showPass)
        self.btn_cancel.clicked.connect(self.cancel)

        # line edits
        self.line_username.textChanged.connect(self.printUsername)
        self.line_password.textChanged.connect(self.printPassword)

        # validators
        self.line_username.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-Z0-9_]+")))

    def getApplicantID(self, applicantID):
        self.applicantID = applicantID

    def printUsername(self):
        self.line_username.setText(self.line_username.text())

    def printPassword(self):
        self.line_password.setText(self.line_password.text())

    def showPass(self):
        if self.check_showPass.isChecked():
            self.line_password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.line_confirmPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        elif not self.check_showPass.isChecked():
            self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.line_confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def createAccount(self):
        applicantID = self.applicantID
        username = self.line_username.text()
        password = self.line_password.text()

        # do duplicates check
        applicants.addNewApplicantAccount(username, password, applicantID)
        messageBox('Success', 'Account created successfully!', 'information', False)

        updateDetails = f'APPLICANT ACCOUNT CREATED. | Applicant ID: {applicantID} - Username: [{username}]'
        adminUpdateLogWindow.logUpdate(updateDetails)
        adminUpdateLogWindow.showUpdates()
        managerDashboardWindow.showUpdates()

        self.close()
        loginWindow.show()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you wish to cancel your application? \n'
                                      'Data will not be saved.',
                      'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class managerDashboardWindow(managerDashboard.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_pendingApplications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_latestUpdates.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # setup log file
        logging.basicConfig(filename='updateLog.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

        # slots and signals

        # buttons
        self.btn_applicantLog.clicked.connect(self.applicantLog)
        self.btn_teamMembers.clicked.connect(self.teamMembers)
        self.btn_dLeaderInfoBank.clicked.connect(self.dLeaderInfoBank)
        self.btn_adminAudits.clicked.connect(self.adminAudits)
        self.btn_adminManagerProfile.clicked.connect(self.adminManagerProfiles)
        self.tbl_pendingApplications.doubleClicked.connect(self.openApplication)
        self.btn_logout.clicked.connect(self.logout)

        # tables
        self.chart_memberStats = QChartView(self.chart_memberStats)
        self.chart_memberStats.setGeometry(self.chart_memberStats.rect())
        self.chart_memberStats.resize(406, 249)

        # show tables
        self.showMemberStats()
        self.pendingApplications()
        self.showUpdates()

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

    def adminAudits(self):
        adminUpdateLogWindow.show()
        adminUpdateLogWindow.setFocus()

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

    def openApplication(self):
        selectedApplicationIndex = self.tbl_pendingApplications.selectionModel().currentIndex()

        if selectedApplicationIndex.isValid():
            application = self.pendingApplicationsTable.data(
                self.pendingApplicationsTable.index(selectedApplicationIndex.row(), 0), QtCore.Qt.DisplayRole)
            print(application)

            # change UI details in application profile
            result = managers.fetchApplicationDetails(application)
            if result:
                (applicantName, applicantMobileNumber, applicantEmail, applicantOccupation, applicantEmployer, team,
                 dleader, responseWhenJesusLord, responseHowJesusLord, responseLoseSalvation,
                 responseMinistryToSalvation, applicationDate) = result

            managerApplicationViewWindow.lbl_name_filler.setText(f'{applicantName}')
            managerApplicationViewWindow.lbl_mobileNumber_filler.setText(f'{applicantMobileNumber}')
            managerApplicationViewWindow.lbl_email_filler.setText(f'{applicantEmail}')
            managerApplicationViewWindow.lbl_occupation_filler.setText(f'{applicantOccupation}')
            managerApplicationViewWindow.lbl_employer_filler.setText(f'{applicantEmployer}')
            managerApplicationViewWindow.lbl_team_filler.setText(f'{team}')
            managerApplicationViewWindow.lbl_dleader_filler.setText(f'{dleader}')

            managerApplicationViewWindow.text_whenJesusLord.setText(f'{responseWhenJesusLord}')
            managerApplicationViewWindow.text_howJesusLord.setText(f'{responseHowJesusLord}')
            managerApplicationViewWindow.text_loseSalvation.setText(f'{responseLoseSalvation}')
            managerApplicationViewWindow.text_ministryToSalvation.setText(f'{responseMinistryToSalvation}')

            managerApplicationViewWindow.lbl_applicationID_filler.setText(f'{application}')
            managerApplicationViewWindow.lbl_dateSubmitted_filler.setText(f'{applicationDate}')

            managerApplicationViewWindow.setWindowTitle(f'{applicantName}')

            managerApplicationViewWindow.show()

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

    def showUpdates(self):
        try:
            # fetch updates from the log file
            with open('updateLog.txt', 'r') as logFile:
                updates = logFile.readlines()

            # display updates in table view
            model = QtGui.QStandardItemModel()
            model.setHorizontalHeaderLabels(['Update Timestamp', 'Action'])

            for update in updates:
                # splitting timestamp and update text / handling fractional seconds by splitting on the comma
                strTimestamp, textUpdate = update.split(' - ', 1)
                strTimestamp, fractionalSeconds = strTimestamp.split(',', 1)

                # parse timestamp, including fractional seconds
                dateTimeTimestamp = (datetime.strptime(strTimestamp, '%Y-%m-%d %H:%M:%S') +
                                     timedelta(microseconds = int(fractionalSeconds)*1000))

                # format timestamp for display
                formattedTimestamp = dateTimeTimestamp.strftime('%Y-%m-%d %H:%M:%S')

                # create items for the table & append to model
                timestampItem = QtGui.QStandardItem(formattedTimestamp)
                detailsItem = QtGui.QStandardItem(textUpdate.strip())
                model.appendRow([timestampItem, detailsItem])

            self.tbl_latestUpdates.setModel(model)
            self.tbl_latestUpdates.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
            self.tbl_latestUpdates.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            print(f'An error has occurred in updating logs: {e}')


    def logout(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class managerApplicationViewWindow(managerApplicationView.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        self.btn_accept.clicked.connect(self.acceptApplication)
        self.btn_reject.clicked.connect(self.rejectApplication)
        self.btn_close.clicked.connect(self.backToDashboard)

    def acceptApplication(self):
        applicationID = self.lbl_applicationID_filler.text()
        applicantName = self.lbl_name_filler.text()
        applicantEmail = self.lbl_email_filler.text()
        team = self.lbl_team_filler.text()

        result = managers.fetchApplicantDetails(applicationID)
        if result:
            firstName, lastName, dob, mobileNumber, teamID, applicantEmail, dleaderIndex = result

        applicantDOB = dob.strftime("%Y-%m-%d")
        print(result, applicantDOB)

        status = "ACCEPTED"

        if messageBox('Confirmation', f'Are you sure you want to approve [{applicantName}]? \n'
                                      f'This action cannot be undone.', 'question',
                      True) == QtWidgets.QMessageBox.Ok:
            managers.modifyApplicationStatus(applicationID, status)
            managers.addNewMember(firstName, lastName, applicantDOB, mobileNumber, teamID, applicantEmail, dleaderIndex)
            messageBox('Success', f'{applicantName} has been approved.', 'information')

            updateDetails = f'APPLICATION APPROVED. | Application ID: {applicationID} - Applicant Name: {applicantName}'
            adminUpdateLogWindow.logUpdate(updateDetails)
            adminUpdateLogWindow.showUpdates()
            managerDashboardWindow.showUpdates()

            managerApplicationViewWindow.close()
            managerDashboardWindow.pendingApplications()
            managerDashboardWindow.show()
            managerDashboardWindow.setFocus()

            # send email to applicant
            emailSubject = f'Application Approved'
            emailBody = f'Dear {applicantName},\n\n' \
                        f'Congratulations! Your application for {team} has been approved.\n\n' \
                        f'Please contact Karen via email (isoceliese@tti.com.ph) for further instructions. ' \
                        f'We hope to see you with us soon!\n\n' \
                        f'Best regards,\n' \
                        f'CCF Live Production Management Team'
            self.sendEmail(applicantEmail, emailSubject, emailBody)
        else:
            self.setFocus()

    def rejectApplication(self):
        applicationID = self.lbl_applicationID_filler.text()
        applicantName = self.lbl_name_filler.text()
        applicantEmail = self.lbl_email_filler.text()
        team = self.lbl_team_filler.text()
        status = "REJECTED"

        if messageBox('Confirmation', f'Are you sure you want to reject [{applicantName}]? \n'
                                      f'This action cannot be undone.', 'question',
                      True) == QtWidgets.QMessageBox.Ok:
            managers.modifyApplicationStatus(applicationID, status)
            messageBox('Success', f'{applicantName} has been rejected.', 'information')

            updateDetails = f'APPLICATION REJECTED. | Application ID: {applicationID} - Applicant Name: {applicantName}'
            adminUpdateLogWindow.logUpdate(updateDetails)
            adminUpdateLogWindow.showUpdates()
            managerDashboardWindow.showUpdates()

            managerApplicationViewWindow.close()
            managerDashboardWindow.pendingApplications()
            managerDashboardWindow.show()
            managerDashboardWindow.setFocus()

            # send email to applicant
            emailSubject = f'Application Rejected'
            emailBody = f'Dear {applicantName},\n\n' \
                        f'We regret to inform you that your application for {team} has been rejected.\n' \
                        f'You may use your applicant credentials to apply again in the future.\n\n' \
                        f'Best regards,\n' \
                        f'CCF Live Production Management Team'
            self.sendEmail(applicantEmail, emailSubject, emailBody)
        else:
            self.setFocus()

    def sendEmail(self, recipient, subject, message):
        if sendEmailMsg(recipient, subject, message):
            messageBox('Success', 'Email sent successfully!', 'information', False)
        else:
            messageBox('Error', 'Failed to send email.', 'critical', False)

    def backToDashboard(self):
        managerDashboardWindow.show()
        self.close()
        managerDashboardWindow.setFocus()


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
            applicantID = self.pendingApplicationsTable.data(
                self.pendingApplicationsTable.index(selectedApplicantIndex.row(), 0), QtCore.Qt.DisplayRole)
            applicantName = self.pendingApplicationsTable.data(
                self.pendingApplicationsTable.index(selectedApplicantIndex.row(), 1), QtCore.Qt.DisplayRole)
            if messageBox('Confirmation', f'Are you sure you want to delete [{applicantName}]? \n'
                                          f'This action cannot be undone.', 'question',
                          True) == QtWidgets.QMessageBox.Ok:
                managers.removeApplicant(applicantID)
                messageBox('Success', f'{applicantName} has been removed.', 'information')

                updateDetails = f'APPLICANT DELETED. | Applicant ID: {applicantID} - Applicant Name: {applicantName}'
                adminUpdateLogWindow.logUpdate(updateDetails)
                adminUpdateLogWindow.showUpdates()
                managerDashboardWindow.showUpdates()

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

                updateDetails = f'MEMBER DELETED. | Member ID: {memberID} - Member Name: {memberName}'
                adminUpdateLogWindow.logUpdate(updateDetails)
                adminUpdateLogWindow.showUpdates()
                managerDashboardWindow.showUpdates()

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

            updateDetails = f'MEMBER PROFILE EDITED. | Member ID: [{member}]'
            adminUpdateLogWindow.logUpdate(updateDetails)
            adminUpdateLogWindow.showUpdates()
            managerDashboardWindow.showUpdates()

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

                updateDetails = f'NEW MEMBER ADDED. | Member Name: {firstName} {surname}'
                adminUpdateLogWindow.logUpdate(updateDetails)
                adminUpdateLogWindow.showUpdates()
                managerDashboardWindow.showUpdates()

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

                updateDetails = f'DLEADER DELETED. | DLeader ID: {dleaderID} - DLeader Name: {dleaderName}'
                adminUpdateLogWindow.logUpdate(updateDetails)
                adminUpdateLogWindow.showUpdates()
                managerDashboardWindow.showUpdates()

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

                updateDetails = f'NEW DLEADER ADDED. | DLeader Name: {firstName} {surname}'
                adminUpdateLogWindow.logUpdate(updateDetails)
                adminUpdateLogWindow.showUpdates()
                managerDashboardWindow.showUpdates()

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

            updateDetails = f'DLEADER PROFILE EDITED. | DLeader ID: [{dleader}]'
            adminUpdateLogWindow.logUpdate(updateDetails)
            adminUpdateLogWindow.showUpdates()
            managerDashboardWindow.showUpdates()

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


class adminUpdateLogWindow(adminUpdateLog.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_updateLog.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        logging.basicConfig(filename='updateLog.txt', level=logging.INFO, format='%(asctime)s,%(message)s')

        # slots and signals

        # buttons
        # self.combo_sort.currentIndexChanged.connect(self.sortUpdates)
        self.btn_backToDashboard.clicked.connect(self.backToDashboard)

        # line edits
        # self.ln_searchBar.textChanged.connect(self.searchUpdates)

        self.showUpdates()

    def showUpdates(self):
        try:
            with open('updateLog.txt', 'r') as logFile:
                updates = logFile.readlines()

            # display updates in table view
            model = QtGui.QStandardItemModel()
            model.setHorizontalHeaderLabels(['Update Timestamp', 'Action'])

            for update in updates:
                # splitting timestamp and update text / handling fractional seconds by splitting on the comma
                strTimestamp, textUpdate = update.split(' - ', 1)
                strTimestamp, fractionalSeconds = strTimestamp.split(',', 1)

                # parse timestamp, including fractional seconds
                dateTimeTimestamp = (datetime.strptime(strTimestamp, '%Y-%m-%d %H:%M:%S') +
                                     timedelta(microseconds = int(fractionalSeconds)*1000))

                # format timestamp for display
                formattedTimestamp = dateTimeTimestamp.strftime('%Y-%m-%d %H:%M:%S')

                # create items for the table & append to model
                timestampItem = QtGui.QStandardItem(formattedTimestamp)
                detailsItem = QtGui.QStandardItem(textUpdate.strip())
                model.appendRow([timestampItem, detailsItem])

            self.tbl_updateLog.setModel(model)
            self.tbl_updateLog.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
            self.tbl_updateLog.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            print(f'An error has occurred in updating logs: {e}')

    def logUpdate(self, update):
        logging.info(update)

    def backToDashboard(self):
        managerDashboardWindow.show()
        self.close()
        managerDashboardWindow.setFocus()


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

                updateDetails = f'MANAGER DELETED. | Manager ID: {managerID} - Manager Name: {managerName}'
                adminUpdateLogWindow.logUpdate(updateDetails)
                adminUpdateLogWindow.showUpdates()
                managerDashboardWindow.showUpdates()

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

                updateDetails = f'NEW MANAGER ADDED. | Manager Name: {firstName} {surname}'
                adminUpdateLogWindow.logUpdate(updateDetails)
                adminUpdateLogWindow.showUpdates()
                managerDashboardWindow.showUpdates()

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

    # login
    loginWindow = loginWindow()

    # applicant
    applicantDashboardWindow = applicantDashboardWindow()
    applicantNewApplicationWindow = applicantNewApplicationWindow()
    applicantAnotherApplicationWindow = applicantAnotherApplicationWindow()
    applicantNewAccountWindow = applicantNewAccountWindow()

    # manager
    managerDashboardWindow = managerDashboardWindow()
    managerApplicationViewWindow = managerApplicationViewWindow()
    managerApplicantLogWindow = managerApplicantLogWindow()
    managerTeamMembersWindow = managerTeamMembersWindow()
    managerAddNewMemberWindow = managerAddNewMemberWindow()
    managerMemberProfileWindow = managerMemberProfileWindow()
    managerEditMemberProfileWindow = managerEditMemberProfileWindow()
    managerDLeaderInfoBankWindow = managerDLeaderInfoBankWindow()
    managerAddNewDLeaderWindow = managerAddNewDLeaderWindow()
    managerDLeaderProfileWindow = managerDLeaderProfileWindow()
    managerEditDLeaderProfileWindow = managerEditDLeaderProfileWindow()

    # admin
    adminUpdateLogWindow = adminUpdateLogWindow()
    adminManagerProfilesWindow = adminManagerProfilesWindow()
    adminRegisterManagerWindow = adminRegisterManagerWindow()

    loginWindow.show()
    sys.exit(app.exec_())
