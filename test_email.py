import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

msg = EmailMessage()
msg["Subject"] = "Pingr / Job Bot Test Email"
msg["From"] = EMAIL_FROM
msg["To"] = EMAIL_TO
msg.set_content("If you received this, SMTP + .env are configured correctly.")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(EMAIL_FROM, SMTP_PASSWORD)
    server.send_message(msg)

print("✅ Test email sent successfully")
