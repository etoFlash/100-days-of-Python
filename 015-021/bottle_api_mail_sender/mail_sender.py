import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os.path import exists


configs = {"smtp_address": "smtp.test.test",
           "smtp_port": "465",
           "sender_email": "test@test.test",
           "password": "test_pass"}


if exists("secrets.cfg"):
    with open("secrets.cfg", "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            configs[key] = value


def send_mail(receiver_email, message_subject="", message_text="", message_html=""):
    message = MIMEMultipart("alternative")
    message["Subject"] = message_subject
    message["From"] = configs["sender_email"]
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    if not message_text:
        message_text = "Test message for empty text"
    if not message_html:
        message_html = """\
        <html>
          <body>
            <p>Test message for empty text</p>
          </body>
        </html>
        """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(message_text, "plain")
    part2 = MIMEText(message_html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(configs["smtp_address"], int(configs["smtp_port"]), context=context) as server:
        server.login(configs["sender_email"], configs["password"])
        server.sendmail(
            configs["sender_email"], receiver_email, message.as_string()
        )
