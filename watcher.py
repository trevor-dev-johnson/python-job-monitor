import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from emailer import send_email
from config import KEYWORDS
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

SEEN_FILE = "seen_jobs.json"

def load_seen() -> set[str]:
    if not os.path.exists(SEEN_FILE):
        return set()

    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            raw = f.read().strip()
            if not raw:
                return set()
            data = json.loads(raw)
            return set(data) if isinstance(data, list) else set()
    except (json.JSONDecodeError, OSError):
        return set()

def save_seen(seen: set[str]) -> None:
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(seen), f, indent=2)

def job_matches(text: str) -> bool:
    text = text.lower()
    return any(k in text for k in KEYWORDS)

def check_company(company, seen):
    response = requests.get(company["url"], headers=HEADERS, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    found = []

    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        href = link["href"]

        if not title or len(title) < 10:
            continue

        if job_matches(title):
            job_id = f"{company['name']}::{title}"
            if job_id not in seen:
                found.append((title, href))
                seen.add(job_id)

    return found

def main():
    with open("companies.json") as f:
        companies = json.load(f)

    seen = load_seen()
    all_new_jobs = []

    for company in companies:
        new_jobs = check_company(company, seen)
        for title, link in new_jobs:
            all_new_jobs.append(f"{company['name']}: {title}\n{link}")

    if all_new_jobs:
        body = "\n\n".join(all_new_jobs)
        send_email(
            subject="🚀 New Backend Job Postings Found",
            body=body
        )

    save_seen(seen)

if __name__ == "__main__":
    main()
