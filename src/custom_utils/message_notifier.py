import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import logging


def send_notification(to,
                      subject,
                      body,
                      username=None,
                      password=None,
                      smtp_server=None,
                      port=None):
    """
    Send an email or text notification to the given recipient.

    email account from which the email or text will be sent.

    param to: str
        the subject of the message (Use '' for no subject)
    param body: str
        the content of the notification message

    optional params:
        param username: str
            the username for the sending email account. If no value is
            specified, then the value in the user's system environment is used.
        param password: str
            the password for the sending email account. If no value is
            specified, the value in the user's system environment is used.
        param smtp_server: str
            The smtp server that will be used to send the message. If no value
            is specified, then the value in the user's system environment is
            used.
        param port: int
            the port associated with the smtp server. This must be set if the
            smtp server is set, and vice versa.

    """
    load_dotenv()
    if username is not None:
        email_username = username
    else:
        email_username = os.getenv("EMAIL_USERNAME")
    if password is not None:
        email_password = password
    else:
        email_password = os.getenv("EMAIL_APP_PASSWORD")
    if smtp_server is not None:
        email_server = smtp_server
    else:
        email_server = os.getenv("GMAIL_SMTP_SERVER")
    if port is not None:
        server_port = port
    else:
        server_port = os.getenv("GMAIL_SMTP_PORT")

    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["from"] = email_username
    msg["to"] = to

    server = smtplib.SMTP(email_server, server_port)
    server.starttls()
    server.login(email_username, email_password)
    server.send_message(msg)
    server.quit()
