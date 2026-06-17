
import pandas as pd
from datetime import datetime

companies = [
    "Atlassian",
    "Canva",
    "Xero",
    "WiseTech",
    "Booking.com",
    "Adyen",
    "SAP",
    "Zalando",
    "HubSpot",
    "Stripe"
]

roles = [
    "Python Backend Engineer",
    "Backend Engineer",
    "Software Engineer",
    "Platform Engineer",
    "Data Engineer"
]

jobs = []

for company in companies:
    for role in roles:
        jobs.append({
            "company": company,
            "role": role,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "status": "NEW"
        })

df = pd.DataFrame(jobs)

df.to_csv("data/jobs.csv", index=False)

print(f"Saved {len(df)} jobs")
