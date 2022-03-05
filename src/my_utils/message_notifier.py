import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import logging


def send_notification(to, subject, body, username=None, password=None, smtp_server=None, port=None):
    """
    Send an email or text notification with the given subject and body to the given recipient.

    This function uses the username and password stored in a .env file for the email account from which the email or text will be sent.

    param to: str
        the address of the recipient of the message
    param subject: str
        the subject of the message (Use '' for no subject)
    param body: str
        the content of the notification message

    optional params:
        param username: str
            the username for the sending email account. If no value is specified, then the value in the user's system environment is used.
        param password: str
            the password for the sending email account. If no value is specified, the value in the user's system environment is used.
        param smtp_server: str
            thethe smtp server that will be used to send the message. If no value is specified, then the value in the user's system environment is used.
        param port: int
            the port assorted with the smtp server. This must be set if the smtp server is set, and vice versa. 

    """
    load_dotenv()
    if not username is None:
        email_username = username
    else:
        email_username = os.getenv("EMAIL_USERNAME")
    if not password is None:
        email_password = password
    else:
        email_password = os.getenv("EMAIL_APP_PASSWORD")
    if not smtp_server is None:
        server = smtp_server
    else:
        server = os.getenv("GMAIL_SMTP_SERVER")
    if not port is None:
        server_port = port
    else:
        smtp_port = os.getenv("GMAIL_SMTP_PORT")

    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["from"] = email_username
    msg["to"] = to

    server = smtplib.SMTP(server, smtp_port)
    server.starttls()
    server.login(email_username, email_password)
    server.send_message(msg)
    server.quit()


def test():
    logging_level = logging.WARNING
    app_logger = logging.getLogger(__name__)
    app_logger.setLevel(logging_level)
    try:
        send_notification("7084751390@tmomail.net",
                          "Test Message", "Hello phone!")
        print("Message sent successfully")
        send_notification("vegetafan5@gmail.com",
                          "Test Message", "Hello email!!")
        print("Message sent successfully")
    except Exception:
        app_logger.exception(
            "An error occurred while trying to send the message.")


if __name__ == "__main__":
    test()
