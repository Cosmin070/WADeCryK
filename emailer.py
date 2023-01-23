import smtplib
import ssl
from email.message import EmailMessage

from models.users import User


def send_register_mail(user: User):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "jumpybugs2123@gmail.com"  # Enter your address
    receiver_email = user.email  # Enter receiver address
    password = "dfjsxsrlonzfchqu"

    msg = EmailMessage()
    msg.set_content("Welcome to CryK!")
    msg['Subject'] = "CryK Registration"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)