# Q4: Job Listings Scraper
# Task: Scrape job listings from a website and save to CSV
# Tools: BeautifulSoup + requests
# Target: TimesJobs (https://www.timesjobs.com)
# Note: Always check robots.txt before scraping any website

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_jobs(keyword="python"):
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}&txtLocation="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    job_cards = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for card in job_cards[:10]:
        try:
            title = card.find("h2").text.strip()
            company = card.find("h3", class_="joblist-comp-name").text.strip()
            skills = card.find("span", class_="srp-skills").text.strip()
            posted = card.find("span", class_="sim-posted").text.strip()
            jobs.append({
                "title": title,
                "company": company,
                "skills": skills,
                "posted": posted
            })
            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Skills: {skills}")
            print(f"Posted: {posted}")
            print("-" * 40)
        except AttributeError:
            continue

    # Save to CSV
    with open("jobs.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "company", "skills", "posted"])
        writer.writeheader()
        writer.writerows(jobs)

    print(f"
Saved {len(jobs)} jobs to jobs.csv")

scrape_jobs("python developer")