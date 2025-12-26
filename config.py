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
SMTP_PORT = int(os.getenv("SMTP_PORT", "0"))
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

missing = [
    name for name, value in {
        "EMAIL_FROM": EMAIL_FROM,
        "EMAIL_TO": EMAIL_TO,
        "SMTP_SERVER": SMTP_SERVER,
        "SMTP_PORT": SMTP_PORT,
        "SMTP_PASSWORD": SMTP_PASSWORD,
    }.items() if not value
]

if missing:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
