import smtplib
from email.message import EmailMessage
from config import EMAIL_FROM, EMAIL_TO, SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD

def send_email(subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_FROM, SMTP_PASSWORD)
        server.send_message(msg)
