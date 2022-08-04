import smtplib, email, time, mycolors
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from body import *
import os
load_dotenv()

os.system('clear')
os.system('toilet --metal "SEND EMAIL GMAIL"')

SMTP_SERVER = "smtp.gmail.com" 
SSL_PORT = 465
fromAddress= os.environ.get('fromAddress')
email_to = 'jorge.chavarriaga@gmail.com'
gmailPwd= os.environ.get('gmailPwd')
sender = fromAddress
pwd =  gmailPwd
subject = "Gmail Test Message"

def emailSenderPlainText(sender, pwd, to, subject, body):
    message = email.message.EmailMessage()
    sender = sender
    pwd = pwd
    recipient = to
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    body = body
    message.set_content(body)
    try:
        mail_server = smtplib.SMTP_SSL(SMTP_SERVER)
        mail_server.login(sender, pwd)
        mail_server.send_message(message)
        mail_server.quit()
        print(mycolors.bcolors.OKGREEN + "[+]        Email Sent" + mycolors.bcolors.ENDC)
        time.sleep(5)
    except:
        print(mycolors.bcolors.FAIL + "[-]      Failed!!!" + mycolors.bcolors.ENDC)
        time.sleep(5)



emailSenderPlainText(sender, pwd, email_to, subject, bodyPlain)

def sendEmailHtml(fromAddress, email_to, html, pwd):
    email_message = MIMEMultipart()
    email_message['From'] = fromAddress
    email_message['To'] = email_to
    email_message['Subject'] = subject
    email_message.attach(MIMEText(html, "html"))
    email_string = email_message.as_string()
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT) as server:
            server.login(fromAddress, pwd)
            server.sendmail(fromAddress, email_to, email_string)
        print(mycolors.bcolors.OKGREEN + "[+]        Email Sent" + mycolors.bcolors.ENDC)
    except:
        print(mycolors.bcolors.FAIL + "[-]      Failed!!!" + mycolors.bcolors.ENDC)


sendEmailHtml(fromAddress, email_to, bodyHtml, pwd)

