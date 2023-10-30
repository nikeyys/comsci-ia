import smtplib
from email.mime.text import MIMEText

def sendEmailMsg(recipient, subject, message):
    smtpServer = 'smtp.gmail.com'
    smtpPort = 587
    smtpUser = 'nicplayzrblxyt@gmail.com'
    smtpPassword = 'yryzyvpuwmzjyjga'

    emailMsg = MIMEText(message)

    emailMsg['From'] = smtpUser
    emailMsg['To'] = recipient
    emailMsg['Subject'] = subject

    server = smtplib.SMTP(smtpServer, smtpPort)
    server.starttls()
    server.login(smtpUser, smtpPassword)

    server.sendmail(smtpUser, recipient, emailMsg.as_string())

    server.quit()

    return True
