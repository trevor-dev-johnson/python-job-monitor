import json
import os
from emailer import send_email
from config import KEYWORDS

COMPANIES_FILE = "companies.json"
SEEN_FILE = "seen_jobs.json"


def load_seen():
    if not os.path.exists(SEEN_FILE):
        return set()
    try:
        with open(SEEN_FILE, "r") as f:
            data = json.load(f)
            return set(data)
    except json.JSONDecodeError:
        return set()


def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f, indent=2)


def main():
    seen = load_seen()

    with open(COMPANIES_FILE, "r") as f:
        companies = json.load(f)

    new_matches = []

    for company in companies:
        for job in company.get("jobs", []):
            title = job["title"].lower()
            if any(keyword in title for keyword in KEYWORDS):
                job_id = f"{company['name']}::{job['title']}::{job['url']}"
                if job_id not in seen:
                    seen.add(job_id)
                    new_matches.append(
                        f"{company['name']} — {job['title']}\n{job['url']}"
                    )

    if new_matches:
        body = "\n\n".join(new_matches)
        send_email(
            subject="🧠 New Backend / Python Jobs Found",
            body=body,
        )

    save_seen(seen)


if __name__ == "__main__":
    main()
