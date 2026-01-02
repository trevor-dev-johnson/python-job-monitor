# Job Watcher

Job Watcher is an automated Python service that monitors real company job boards for backend-relevant roles and delivers daily email alerts. It runs fully unattended using GitHub Actions, persists state to prevent duplicate notifications, and is designed to be reliable, low-noise, and production-aligned.

This project focuses on automation, correctness, and real-world backend patterns rather than UI or product features.

---

## Features

- Daily automated job monitoring via GitHub Actions
- Fetches live job data from real company job boards (Greenhouse)
- Keyword-based role filtering (backend, Python, API, platform, etc.)
- Persistent state to prevent duplicate notifications
- Email alerts only when new matching jobs are found
- Secure secret handling using GitHub Actions secrets
- Idempotent and fault-tolerant execution

---

## Tech Stack

- Python 3.12
- Requests – HTTP client
- GitHub Actions – scheduling and automation
- SMTP (Gmail) – email delivery
- JSON – lightweight persistent state
- Greenhouse API – job data source

---

## How It Works

1. GitHub Actions runs the workflow on a daily schedule.
2. The watcher fetches job listings from configured company boards.
3. Job titles are filtered using a defined set of keywords.
4. New jobs are compared against previously seen jobs.
5. If new matches exist:
   - An email is sent with job titles and links.
   - Seen jobs are persisted back to the repository.
6. If no new jobs are found, the run completes quietly.

This ensures clean notifications with no repeated alerts.

---

## Project Structure

.
├── .github/workflows/
│ └── daily_job_alert.yml
├── job_sources/
│ └── greenhouse.py
├── companies.json
├── config.py
├── emailer.py
├── watcher.py
├── seen_jobs.json
├── requirements.txt
└── README.md

yaml
Copy code

---

## Configuration

### Keywords

Edit `config.py` to control which roles are matched:

```python
KEYWORDS = [
    "backend",
    "python",
    "software engineer",
    "api",
    "platform"
]
Email Settings
Email credentials are injected securely using GitHub Actions secrets:

EMAIL_FROM

EMAIL_TO

SMTP_SERVER

SMTP_PORT

SMTP_PASSWORD

No credentials are committed to the repository.

Running Locally (Optional)
bash
Copy code
pip install -r requirements.txt
python watcher.py
Environment variables must be set locally if testing email delivery.

Automation
The service runs daily via GitHub Actions using a scheduled workflow.
State changes to seen_jobs.json are automatically committed back to the repository to prevent duplicate alerts across runs.

Design Goals
Reliability over features

Clean, idempotent execution

Minimal notification noise

Production-aligned automation patterns

Clear separation of concerns
