import smtplib
import os
from email.message import EmailMessage

def send(message, to_addrs, subject = 'SentiGo: Event Advisor'):
    msg = EmailMessage()
    msg.set_content(message)
    email_sender = os.environ.get("EMAIL_SENDER")
    password = os.environ.get("EMAIL_PASSWORD")

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email_sender, password)
        msg['Subject'] = subject
        server.send_message(msg = msg, from_addr = email_sender, to_addrs = to_addrs)
    except:
        print('Email could not be sent')