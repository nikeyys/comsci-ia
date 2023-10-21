from classes.database import *


class general:
    @staticmethod
    def verifyLogin(user, passw, loginType):
        with ConnectionPool() as cursor:
            if loginType == 'applicant':
                cursor.execute(
                    '''SELECT "applicantPassword" FROM "applicantCredentials" WHERE "applicantUsername" = %s''',
                    (user,))
            elif loginType == 'manager':
                cursor.execute('''SELECT "managerPassword" FROM manager WHERE "managerUsername" = %s''', (user,))

            result = cursor.fetchone()
            if result is not None:
                if passw == result[0]:
                    return True
                else:
                    return False

    @staticmethod
    def insertApplicantCredentials(user, passw):
        with ConnectionPool() as cursor:
            cursor.execute(
                '''INSERT INTO "applicantCredentials"("applicantUsername", "applicantPassword") VALUES(%s,%s)''',
                (user, passw))

    @staticmethod
    def insertManagerCredentials(user, passw, firstName, surname):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO manager("managerUsername", "managerPassword", "managerFirstName", 
            "managerSurname") VALUES(%s,%s,%s,%s)''', (user, passw, firstName, surname))


class applicants:
    @staticmethod
    def getPreviousApplications():
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT "applicationID", "applicationDate", team."teamName", "applicationStatus" 
            FROM application
            INNER JOIN team ON application."teamID" = team."teamID"''', ())
            return cursor.fetchall()

    @staticmethod
    def fetchApplicantDetails(user):
        with ConnectionPool() as cursor:
            cursor.execute(
                '''SELECT CONCAT(UPPER("applicantSurname"), ', ', "applicantFirstName") AS "applicantName", 
                applicant."applicantID", CONCAT(UPPER("dleaderSurname"), ', ', "dleaderFirstName") AS "dleaderName", 
                "applicantMobileNumber", "applicantEmail", "applicantDOB"
                FROM applicant 
                INNER JOIN "applicantCredentials" ON applicant."applicantID" = "applicantCredentials"."applicantID"
                FULL OUTER JOIN "dleader" ON applicant."dleaderID" = dleader."dleaderID"
                WHERE "applicantUsername" = %s''', (user,))
            row = cursor.fetchone()
            if row is not None:
                applicantName = row[0]
                applicantID = row[1]
                dleaderName = row[2] if row[2] != ", " else 'No DLeader assigned.'
                applicantMobileNumber = row[3]
                applicantEmail = row[4] if row[4] is not None else 'No email provided.'
                applicantDOB = row[5]
                return applicantName, applicantID, dleaderName, applicantMobileNumber, applicantEmail, applicantDOB
            else:
                return None


class managers:
    @staticmethod
    def getPendingApplications(keyword=None):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT "applicationID", CONCAT(applicant."applicantFirstName", ' ',
            applicant."applicantSurname") AS "applicantName", "applicationDate", team."teamName" 
            FROM application
            INNER JOIN applicant ON application."applicantID" = applicant."applicantID"
            INNER JOIN team ON application."teamID" = team."teamID"
            WHERE application."applicationStatus" = 'Pending'  /* AND (applicant."applicantFirstName" ILIKE %s 
            OR applicant."applicantSurname" ILIKE %s) */
            ORDER BY "applicationID"''', (f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    @staticmethod
    def getApplicants(keyword=None):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT applicant."applicantID", CONCAT(applicant."applicantFirstName", ' ', applicant."applicantSurname") 
            AS "applicantName", "applicantMobileNumber", team."teamName"
            FROM applicant
            INNER JOIN application ON applicant."applicantID" = application."applicantID"
            INNER JOIN team ON applicant."teamID" = team."teamID"
            WHERE applicant."applicantFirstName" ILIKE %s OR applicant."applicantSurname" ILIKE %s
            ORDER BY "applicationID"''', (f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    @staticmethod
    def getTeamMembers(keyword):
        with ConnectionPool() as cursor:
            cursor.execute('''
                SELECT "memberID", CONCAT("memberFirstName", ' ', "memberSurname") AS "memberName", team."teamName"
                FROM member
                INNER JOIN team ON member."teamID" = team."teamID"
                WHERE member."memberFirstName" ILIKE %s OR member."memberSurname" ILIKE %s
                ORDER BY "memberID"''',
                           (f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    @staticmethod
    def getMemberStats():
        with ConnectionPool() as cursor:
            cursor.execute('''
                SELECT "teamName", COUNT(*) FROM member 
                JOIN team ON member."teamID" = team."teamID"
                GROUP BY "teamName"''')
            rows = cursor.fetchall()

        teams = [row[0] for row in rows]
        memberCounts = [row[1] for row in rows]

        return teams, memberCounts

    @staticmethod
    def addNewMember(firstName, lastName, dob, mobileNumber, team, email, dleaderIndex):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO member("memberFirstName", "memberSurname", "memberDOB", "memberMobileNumber",
            "teamID", "memberEmail", "dleaderID") VALUES(%s,%s,%s,%s,%s,%s,%s)''', (firstName, lastName, dob,
                                                                                   mobileNumber, team,
                                                                                   email, dleaderIndex))

    @staticmethod
    def fetchManagerDetails(user):
        with ConnectionPool() as cursor:
            cursor.execute(
                '''SELECT "managerFirstName" AS "managerName" FROM manager 
                WHERE "managerUsername" = %s''', (user,))
            row = cursor.fetchone()
        if row is not None:
            managerName = row[0]
            return managerName
        else:
            return None

    @staticmethod
    def removeApplicant(applicantID):
        with ConnectionPool() as cursor:
            cursor.execute('''
            DELETE FROM applicant WHERE "applicantID" = %s
            ''', (applicantID,))

    @staticmethod
    def fetchMemberDetails(member):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT CONCAT(UPPER("memberSurname"), ', ', "memberFirstName") AS "memberName", member."memberID", 
            team."teamName", "memberDOB", ((CURRENT_DATE- "memberDOB")/365) AS "memberAge", "memberMobileNumber", 
            "memberEmail", CONCAT("dleaderSurname", ', ', "dleaderFirstName") AS "dleaderName"
            FROM member
            INNER JOIN team ON member."teamID" = team."teamID"
            LEFT JOIN dleader ON dleader."dleaderID" = member."dleaderID"
            WHERE "memberID" = %s''', (member,))
            row = cursor.fetchone()
        if row is not None:
            memberName = row[0]
            memberID = row[1]
            teamName = row[2]
            memberDOB = row[3]
            memberAge = row[4]
            memberMobileNumber = row[5]
            memberEmail = row[6] if row[6] is not None else 'No email provided.'
            dleaderName = row[7] if row[7] != ", " else 'No DLeader assigned.'
            return memberName, memberID, teamName, memberDOB, memberAge, memberMobileNumber, memberEmail, dleaderName


class administrators:
    @staticmethod
    def add(firstName, lastName, username, password):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO manager("managerFirstName", "managerSurname", "managerUsername", 
            "managerPassword") VALUES(%s,%s,%s,%s)''', (firstName, lastName, username, password))

    @staticmethod
    def getManagerProfiles(keyword):
        with ConnectionPool() as cursor:
            cursor.execute('''
                SELECT "managerID", CONCAT("managerFirstName", ' ', "managerSurname") AS "managerName", "managerUsername"
                FROM manager
                WHERE manager."managerFirstName" ILIKE %s OR manager."managerSurname" ILIKE %s OR 
                manager."managerUsername" ILIKE %s
                ORDER BY "managerID"
                ''', (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    @staticmethod
    def removeManager(manID):
        with ConnectionPool() as cursor:
            cursor.execute('''DELETE FROM manager WHERE "managerID" = %s''', (manID,))



if __name__ == '__main__':
    Database.initialize(database='ccf-volunteers', user='postgres', password='543738', host='localhost', port='5432')
