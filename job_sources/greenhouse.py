import requests

def fetch_greenhouse_jobs(board_slug):
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_slug}/jobs"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    jobs = []
    for job in response.json().get("jobs", []):
        jobs.append({
            "title": job["title"],
            "url": job["absolute_url"],
            "location": job["location"]["name"].lower()
        })

    return jobs
