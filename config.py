import os

KEYWORDS = [
    "backend",
    "python",
    "software engineer",
    "api",
    "platform",
]

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

if not all([EMAIL_FROM, EMAIL_TO, SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD]):
    raise RuntimeError("Missing required email environment variables")
