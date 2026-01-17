# 🔍 Job Watcher

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)](https://www.python.org/)
[![GitHub Actions](https://img.shields.io/badge/Automation-GitHub_Actions-2088FF?style=flat-square&logo=github-actions)](https://github.com/features/actions)

**Job Watcher** is an automated Python service that monitors real company job boards for backend-related roles and sends daily email alerts when new matching positions are posted. It runs on a scheduled GitHub Actions workflow and persists state to prevent duplicate notifications.

This project focuses on **backend automation**, **correctness**, and **real-world system behavior** rather than UI or product features.

---

## ✨ Features

- **Daily automated job monitoring** via GitHub Actions
- **Fetches live job listings** from real company job boards (Greenhouse)
- **Keyword-based filtering** for backend-relevant roles
- **Persistent state** to avoid duplicate job alerts
- **Email notifications** sent only when new matches are found
- **Secure secret handling** using GitHub Actions secrets

---

## 🛠 Tech Stack

- **Python 3.12**
- **Requests**
- **GitHub Actions**
- **SMTP (Gmail)**
- **Greenhouse Jobs API**

---

## ⚙️ How It Works



1. **GitHub Actions** runs the watcher on a daily schedule.
2. **Job listings** are fetched from configured company boards.
3. **Job titles** are filtered using predefined keywords.
4. **New jobs** are compared against previously seen listings.
5. **If new matches exist:**
   - An email is sent with job titles and links.
   - Seen jobs are committed back to the repository.
6. **If no new jobs are found**, the run completes quietly.

---

## 🚀 Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/job-watcher.git](https://github.com/your-username/job-watcher.git)
Configure Secrets: Add your EMAIL_USER, EMAIL_PASSWORD, and RECIPIENT_EMAIL to your GitHub Repository Secrets.

Schedule: The service is pre-configured to run daily via .github/workflows/main.yml.
