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
    def populateDLeaderCombo():
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT CONCAT("dleaderFirstName", ' ', "dleaderSurname") AS "dleaderName" 
            FROM dleader
            ORDER BY "dleaderName" ASC''', ())
            return cursor.fetchall()

    @staticmethod
    def getDLeaderID(dleaderName):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT "dleaderID" FROM dleader
            WHERE CONCAT("dleaderFirstName", ' ', "dleaderSurname") = %s''', (dleaderName,))
            return cursor.fetchone()[0]

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
                applicantEmail = row[4]
                applicantDOB = row[5]
                return applicantName, applicantID, dleaderName, applicantMobileNumber, applicantEmail, applicantDOB
            else:
                return None

    @staticmethod
    def getApplicants(keyword=None):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT applicant."applicantID", CONCAT(applicant."applicantFirstName", ' ', applicant."applicantSurname") 
            AS "applicantName", "applicantMobileNumber", team."teamName"
            FROM applicant
            INNER JOIN application ON applicant."applicantID" = application."applicantID"
            INNER JOIN team ON application."teamID" = team."teamID"
            WHERE applicant."applicantFirstName" ILIKE %s OR applicant."applicantSurname" ILIKE %s OR 
            applicant."applicantEmail" ILIKE %s OR applicant."applicantMobileNumber" ILIKE %s
            ORDER BY "applicationID"''', (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    @staticmethod
    def addNewApplicantProfile(firstName, surname, mobileNumber, email, dob, dleaderID, occupation, employer):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO applicant("applicantFirstName", "applicantSurname", "applicantMobileNumber", 
                            "applicantEmail", "applicantDOB", "dleaderID", "applicantOccupation", 
                            "applicantEmployer") 
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
                            SELECT LASTVAL()''', (firstName, surname, mobileNumber, email, dob,
                                                              dleaderID, occupation, employer))
            return cursor.fetchone()[0]

    @staticmethod
    def addNewApplication(whenJesusLord, howJesusLord, loseSalvation, ministryToSalvation, applicationDate, applicantID,
                          teamID):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO application("whenJesusLord", "howJesusLord", "loseSalvation", 
                            "ministryToSalvation", "applicationDate", "applicantID", "teamID", "applicationStatus") 
                            VALUES(%s,%s,%s,%s,%s,%s,%s, 'PENDING')''',
                           (whenJesusLord, howJesusLord, loseSalvation, ministryToSalvation, applicationDate,
                            applicantID, teamID))

    @staticmethod
    def addNewApplicantAccount(username, password, applicantID):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO "applicantCredentials"("applicantUsername", "applicantPassword", 
            "applicantID") VALUES(%s,%s,%s)''', (username, password, applicantID))


class managers:
    @staticmethod
    def getPermissionLevel(manager):
        with ConnectionPool() as cursor:
            cursor.execute('''SELECT "permissionLevel" FROM manager WHERE "managerUsername" = %s''', (manager,))
            result = cursor.fetchone()
        if result is not None:
            permission = result[0]
            return permission
        else:
            return None

    @staticmethod
    def getPendingApplications(keyword=None):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT "applicationID", CONCAT(applicant."applicantFirstName", ' ',
            applicant."applicantSurname") AS "applicantName", "applicationDate", team."teamName" 
            FROM application
            INNER JOIN applicant ON application."applicantID" = applicant."applicantID"
            INNER JOIN team ON application."teamID" = team."teamID"
            WHERE application."applicationStatus" = 'PENDING'  /* AND (applicant."applicantFirstName" ILIKE %s 
            OR applicant."applicantSurname" ILIKE %s) */
            ORDER BY "applicationID"''', (f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    @staticmethod
    def fetchApplicationDetails(application):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT CONCAT(applicant."applicantFirstName", ' ', applicant."applicantSurname") 
            AS "applicantName", applicant."applicantMobileNumber", applicant."applicantEmail", 
            applicant."applicantOccupation", applicant."applicantEmployer", team."teamName", 
            CONCAT(dleader."dleaderFirstName", ' ', dleader."dleaderSurname") AS "dleaderName", "whenJesusLord", 
            "howJesusLord", "loseSalvation", "ministryToSalvation", "applicationDate" 
            FROM application
            LEFT JOIN applicant ON application."applicantID" = applicant."applicantID"
            INNER JOIN team ON application."teamID" = team."teamID"
            LEFT JOIN dleader ON applicant."dleaderID" = dleader."dleaderID"
            WHERE "applicationID" = %s''', (application,))
            row = cursor.fetchone()
        if row is not None:
            applicantName = row[0]
            applicantMobileNumber = row[1]
            applicantEmail = row[2]
            applicantOccupation = row[3]
            applicantEmployer = row[4]
            teamName = row[5]
            dleaderName = row[6] if row[6] != " " else 'No DLeader assigned.'
            whenJesusLord = row[7]
            howJesusLord = row[8]
            loseSalvation = row[9]
            ministryToSalvation = row[10]
            applicationDate = row[11]
            return (applicantName, applicantMobileNumber, applicantEmail, applicantOccupation, applicantEmployer,
                    teamName, dleaderName, whenJesusLord, howJesusLord, loseSalvation, ministryToSalvation,
                    applicationDate)

    @staticmethod
    def fetchApplicantDetails(application):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT "applicantFirstName", "applicantSurname", "applicantDOB", "applicantMobileNumber", "applicantEmail",
            team."teamID", "dleaderID"
            FROM applicant
            INNER JOIN application ON applicant."applicantID" = application."applicantID"
            INNER JOIN team ON application."teamID" = team."teamID"
            WHERE "applicationID" = %s''', (application,))
            row = cursor.fetchone()
        if row is not None:
            applicantFirstName = row[0]
            applicantSurname = row[1]
            applicantDOB = row[2]
            applicantMobileNumber = row[3]
            applicantEmail = row[4]
            teamID = row[5]
            dleaderID = row[6] if row[6] is not None else None
            return (applicantFirstName, applicantSurname, applicantDOB, applicantMobileNumber, teamID, applicantEmail,
                    dleaderID)

    @staticmethod
    def modifyApplicationStatus(application, status):
        with ConnectionPool() as cursor:
            cursor.execute('''UPDATE application SET "applicationStatus" = %s WHERE "applicationID" = %s''',
                           (status, application))

    @staticmethod
    def getApplicants(keyword=None):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT applicant."applicantID", CONCAT(applicant."applicantFirstName", ' ', applicant."applicantSurname") 
            AS "applicantName", "applicantMobileNumber", team."teamName"
            FROM applicant
            INNER JOIN application ON applicant."applicantID" = application."applicantID"
            INNER JOIN team ON application."teamID" = team."teamID"
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
            cursor.execute('''
            INSERT INTO member("memberFirstName", "memberSurname", "memberDOB", "memberMobileNumber", "teamID", 
            "memberEmail", "dleaderID") 
            VALUES(%s,%s,%s,%s,%s,%s,%s)''', (firstName, lastName, dob, mobileNumber, team, email, dleaderIndex))

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
    def removeMember(memberID):
        with ConnectionPool() as cursor:
            cursor.execute('''DELETE FROM member WHERE "memberID" = %s''', (memberID,))

    @staticmethod
    def removeApplicant(applicantID):
        with ConnectionPool() as cursor:
            cursor.execute('''DELETE FROM applicant WHERE "applicantID" = %s''', (applicantID,))

    @staticmethod
    def fetchMemberDetails(member):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT CONCAT(UPPER("memberSurname"), ', ', "memberFirstName") AS "memberName", member."memberID", 
            team."teamName", "memberDOB", ((CURRENT_DATE- "memberDOB")/365) AS "memberAge", "memberMobileNumber", 
            "memberEmail", CONCAT("dleaderFirstName", ' ', "dleaderSurname") AS "dleaderName"
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
            dleaderName = row[7] if row[7] != " " else 'No DLeader assigned.'
            return memberName, memberID, teamName, memberDOB, memberAge, memberMobileNumber, memberEmail, dleaderName

    @staticmethod
    def editMemberProfile(teamID, dleaderID, dob, mobileNumber, email, member):
        with ConnectionPool() as cursor:
            cursor.execute('''
            UPDATE member
            SET "memberDOB" = CASE WHEN %s = '' THEN "memberDOB" ELSE %s END, 
                "memberMobileNumber" = CASE WHEN %s = '' THEN "memberMobileNumber" ELSE %s END, 
                "memberEmail" = CASE WHEN %s = '' THEN "memberEmail" ELSE %s END, 
                "dleaderID" = %s, 
                "teamID" = %s
            WHERE "memberID" = %s''',
                           (dob, dob, mobileNumber, mobileNumber, email, email, dleaderID, teamID, member))

    @staticmethod
    def getDLeaders(keyword):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT "dleaderID", CONCAT("dleaderFirstName", ' ', "dleaderSurname") AS "dleaderName" FROM dleader
            WHERE "dleaderFirstName" ILIKE %s OR "dleaderSurname" ILIKE %s''', (f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    @staticmethod
    def fetchDLeaderDetails(dleader):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT CONCAT(UPPER("dleaderSurname"), ', ', "dleaderFirstName") AS "dleaderName", "dleaderID", 
            "dleaderMobileNumber", "dleaderEmail"
            FROM dleader
            WHERE "dleaderID" = %s''', (dleader,))
            row = cursor.fetchone()
        if row is not None:
            dleaderName = row[0]
            dleaderID = row[1]
            dleaderMobileNumber = row[2]
            dleaderEmail = row[3] if row[3] is not None else 'No email provided.'
            return dleaderName, dleaderID, dleaderMobileNumber, dleaderEmail

    @staticmethod
    def fetchDLeaderMembers(dleader, keyword):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT "memberID", CONCAT("memberFirstName", ' ', "memberSurname") AS "memberName", team."teamName"
            FROM member
            INNER JOIN team ON member."teamID" = team."teamID"
            WHERE "dleaderID" = %s AND ("memberFirstName" ILIKE %s OR "memberSurname" ILIKE %s)''',
                           (dleader, f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    @staticmethod
    def addNewDLeader(firstName, surname, mobileNumber, email):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO dleader("dleaderFirstName", "dleaderSurname", "dleaderMobileNumber", 
            "dleaderEmail") VALUES (%s, %s, %s, %s)''', (firstName, surname, mobileNumber, email))

    @staticmethod
    def editDLeaderProfile(mobileNumber, email, dleader):
        with ConnectionPool() as cursor:
            cursor.execute('''UPDATE dleader
            SET "dleaderMobileNumber" = CASE WHEN %s = '' THEN "dleaderMobileNumber" ELSE %s END, 
                "dleaderEmail" = CASE WHEN %s IS NULL THEN "dleaderEmail" ELSE %s END
            WHERE "dleaderID" = %s''', (mobileNumber, mobileNumber, email, email, dleader))

    @staticmethod
    def removeDLeader(dleaderID):
        with ConnectionPool() as cursor:
            cursor.execute('''DELETE FROM dleader WHERE "dleaderID" = %s''', (dleaderID,))

    @staticmethod
    def populateMemberCombo():
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT CONCAT("memberFirstName", ' ', "memberSurname") AS "memberName" 
            FROM member
            WHERE "dleaderID" IS NULL
            ORDER BY "memberName" ASC
            ''', ())
            return cursor.fetchall()

    @staticmethod
    def getMemberID(memberName):
        with ConnectionPool() as cursor:
            cursor.execute('''
            SELECT "memberID" FROM member
            WHERE CONCAT("memberFirstName", ' ', "memberSurname") = %s''', (memberName,))
            return cursor.fetchone()

    @staticmethod
    def addMemberToDLeader(member, dleader):
        with ConnectionPool() as cursor:
            cursor.execute('''
            UPDATE member 
            SET "dleaderID" = %s 
            WHERE "memberID" = %s''', (dleader, member))

    @staticmethod
    def removeMemberFromDLeader(member):
        with ConnectionPool() as cursor:
            cursor.execute('''
            UPDATE member 
            SET "dleaderID" = NULL 
            WHERE "memberID" = %s''', (member,))


class administrators:
    @staticmethod
    def add(firstName, lastName, username, password, permissionLevel):
        with ConnectionPool() as cursor:
            cursor.execute('''INSERT INTO manager("managerFirstName", "managerSurname", "managerUsername", 
            "managerPassword", "permissionLevel") VALUES(%s,%s,%s,%s,%s)''',
                           (firstName, lastName, username, password, permissionLevel))

    @staticmethod
    def getManagerProfiles(keyword):
        with ConnectionPool() as cursor:
            cursor.execute('''
                SELECT "managerID", CONCAT("managerFirstName", ' ', "managerSurname") AS "managerName", "managerUsername", "permissionLevel"
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


class miscellaneous:
    @staticmethod
    def actionLog(user, action, tableChanged, description, timestamp):
        with ConnectionPool() as cursor:
            cursor.execute('''
            INSERT INTO "auditLog"("managerID", "actionID", "affectedTable", description, timestamp)
            VALUES(%s,%s,%s,%s,%s)''', (user, action, tableChanged, description, timestamp))


if __name__ == '__main__':
    Database.initialize(database='ccf-volunteers', user='postgres', password='543738', host='localhost', port='5432')
