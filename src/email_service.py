import os
from email.mime.text import MIMEText
import smtplib
from log import LogUtils as log

sender = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("EMAIL_RECIPIENT")
host = os.getenv("SSL_SMTP_HOST")
port = int(os.getenv("SSL_SMTP_PORT"))


class EmailService:
    def __init__(self, subject, message, attach=None):
        self.message = message
        self.subject = subject
        self.attach = attach

    def send(self):
        to_addrs = recipient.split(";")
        log("Try send email...")
        try:
            to_addrs = recipient.split(";")

            message = MIMEText(self.message + "\n\n\n\n Email sent automatically")
            message["subject"] = self.subject
            message["from"] = sender
            message["to"] = ", ".join(to_addrs)

            server = smtplib.SMTP_SSL(host, port)
            server.login(sender, password)
            server.sendmail(sender, to_addrs, message.as_string())

            server.quit()
        except Exception as err:
            log(f"Exception sending email with erros >>> {err}")

    def attachment(self):
        attach = self.attach
        pass
