import requests
from bs4 import BeautifulSoup
import datetime

headers = {"User-Agent": "Mozilla/5.0"}

URLS = [
    ("SEEK AU - RN Sponsorship", "https://www.seek.com.au/jobs?keywords=registered+nurse+visa+sponsorship&daterange=3"),
    ("SEEK AU - HCA 482", "https://www.seek.com.au/jobs?keywords=HCA+482+sponsorship&daterange=3"),
    ("SEEK NZ - RN AEWV", "https://www.seek.co.nz/jobs?keywords=registered+nurse+AEWV&daterange=3"),
    ("SEEK NZ - HCA Visa", "https://www.seek.co.nz/jobs?keywords=health+care+assistant+visa+sponsorship&daterange=3"),
    ("Indeed AU - Aged Care 482", "https://au.indeed.com/jobs?q=aged+care+482+sponsorship&fromage=3"),
    ("Indeed NZ - HCA Sponsorship", "https://nz.indeed.com/jobs?q=health+care+assistant+visa+sponsorship&fromage=3"),
]

today = datetime.date.today()
results = []
results.append(f"KARTIK JOB MONITOR — {today}\n")
results.append("NCNZ APC: 367690 | AHPRA: NMW0004061692\n")
results.append("="*50 + "\n\n")

for platform, url in URLS:
    results.append(f"\n--- {platform} ---\n")
    results.append(f"LINK: {url}\n")
    try:
        res = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(res.text, "html.parser")
        found = 0
        for a in soup.find_all("a", href=True):
            title = a.get_text(strip=True)
            if len(title) > 10 and len(title) < 100:
                low = title.lower()
                if any(w in low for w in ["nurse","care","hca","ain","carer","support"]):
                    link = a["href"]
                    if link.startswith("/"):
                        base = "https://www.seek.com.au" if "seek.com.au" in url else \
                               "https://www.seek.co.nz" if "seek.co.nz" in url else \
                               "https://au.indeed.com" if "indeed.com" in url else ""
                        link = base + link
                    if link.startswith("http"):
                        results.append(f"  JOB: {title}\n  URL: {link}\n\n")
                        found += 1
                        if found >= 10:
                            break
        if found == 0:
            results.append(f"  Visit directly: {url}\n")
    except Exception as e:
        results.append(f"  Error: {e}\n  Visit: {url}\n")

# Always write file
with open("jobs.txt", "w", encoding="utf-8") as f:
    f.writelines(results)

print(f"Done! Found jobs saved to jobs.txt")
