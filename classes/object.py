from classes.database import *


def insertApplicantCredentials(user, passw):
    with ConnectionPool() as cursor:
        cursor.execute('''INSERT INTO "applicantCredentials"("applicantUsername", "applicantPassword") VALUES(%s,%s)''',
                       (user, passw))


def insertManagerCredentials(user, passw, firstName, surname):
    with ConnectionPool() as cursor:
        cursor.execute('''INSERT INTO manager("managerUsername", "managerPassword", "managerFirstName", 
        "managerSurname") VALUES(%s,%s,%s,%s)''', (user, passw, firstName, surname))


def verifyLogin(user, passw, loginType):
    with ConnectionPool() as cursor:
        if loginType == 'applicant':
            cursor.execute('''SELECT "applicantPassword" FROM "applicantCredentials" WHERE "applicantUsername" = %s''',
                           (user,))
        elif loginType == 'manager':
            cursor.execute('''SELECT "managerPassword" FROM manager WHERE "managerUsername" = %s''', (user,))

        result = cursor.fetchone()
        if result is not None:
            if passw == result[0]:
                return True
            else:
                return False


def getPreviousApplications():
    with ConnectionPool() as cursor:
        cursor.execute('''SELECT "applicationID", "applicationDate", "teamID", "applicationStatus" FROM application''')
        return cursor.fetchall()


def getPendingApplications(keyword=None):
    with ConnectionPool() as cursor:
        cursor.execute('''
        SELECT "applicationID", CONCAT(applicant."applicantFirstName", ' ',
        applicant."applicantSurname") AS "applicantName", "applicationDate", applicant."teamID" 
        FROM application
        INNER JOIN applicant ON application."applicantID" = applicant."applicantID"
        WHERE application."applicationStatus" = 'Pending' AND (applicant."applicantFirstName" ILIKE %s 
        OR applicant."applicantSurname" ILIKE %s)''', (f'%{keyword}%', f'%{keyword}%'))
        return cursor.fetchall()


def getTeamMembers(keyword):
    with ConnectionPool() as cursor:
        cursor.execute('''
            SELECT "memberID", CONCAT("memberFirstName", ' ', "memberSurname") AS "memberName", team."teamName"
            FROM member
            INNER JOIN team ON member."teamID" = team."teamID"
            WHERE member."memberFirstName" ILIKE %s OR member."memberSurname" ILIKE %s''',
                       (f'%{keyword}%', f'%{keyword}%'))
        return cursor.fetchall()


def getManagerProfiles(keyword):
    with ConnectionPool() as cursor:
        cursor.execute('''
            SELECT "managerID", CONCAT("managerFirstName", ' ', "managerSurname") AS "managerName", "managerUsername"
            FROM manager
            WHERE manager."managerFirstName" ILIKE %s OR manager."managerSurname" ILIKE %s
            ''', (f'%{keyword}%', f'%{keyword}%'))
        return cursor.fetchall()


class managers:
    @staticmethod
    def add(firstName, lastName, username, password):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO manager("managerFirstName", "managerSurname", "managerUsername", 
            "managerPassword") VALUES(%s,%s,%s,%s)''', (firstName, lastName, username, password))


if __name__ == '__main__':
    Database.initialize(database='ccf-volunteers', user='postgres', password='543738', host='localhost', port='5432')
