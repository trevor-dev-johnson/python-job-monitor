import json
import os
from emailer import send_email
from config import KEYWORDS, SEND_HEARTBEAT
from job_sources.greenhouse import fetch_greenhouse_jobs

COMPANIES_FILE = "companies.json"
SEEN_FILE = "seen_jobs.json"


def load_seen():
    if not os.path.exists(SEEN_FILE):
        return set()

    try:
        with open(SEEN_FILE, "r") as f:
            data = json.load(f)
            return set(data)
    except (json.JSONDecodeError, ValueError):
        # Handles empty or corrupted file
        return set()


def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f, indent=2)


def main():
    print("🚀 Job watcher started")

    seen = load_seen()
    print(f"Loaded {len(seen)} previously seen jobs")

    with open(COMPANIES_FILE, "r") as f:
        companies = json.load(f)

    new_matches = []

    for company in companies:
        name = company["name"]
        provider = company.get("provider")

        print(f"🔍 Checking {name}")

        try:
            if provider == "greenhouse":
                jobs = fetch_greenhouse_jobs(company["board"])
            else:
                print(f"⏭ Skipping {name} (provider not implemented: {provider})")
                continue
        except Exception as e:
            print(f"⚠️ Failed to fetch jobs for {name}: {e}")
            continue

        for job in jobs:
            title = job["title"].lower()

            if any(keyword in title for keyword in KEYWORDS):
                job_id = f"{name}::{job['title']}::{job['url']}"

                if job_id not in seen:
                    seen.add(job_id)
                    new_matches.append(
                        f"{name} — {job['title']}\n{job['url']}"
                    )

    if new_matches:
        print(f"📬 Sending email with {len(new_matches)} new jobs")

        body = "\n\n".join(new_matches)
        send_email(
            subject="🧠 New Backend / Python Jobs Found",
            body=body,
        )
    else:
        print("ℹ️ No new matching jobs found")

        if SEND_HEARTBEAT:
            try:
                send_email(
                    subject="📡 Job Monitor Ran — No Matches Today",
                    body="The job watcher ran successfully but found no new matching jobs."
                )
            except Exception as e:
                print(f"⚠️ Heartbeat email failed: {e}")

    save_seen(seen)
    print("✅ Job watcher finished successfully")


if __name__ == "__main__":
    main()
