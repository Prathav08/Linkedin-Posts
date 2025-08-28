import schedule
import time
from raindrop_fetcher import fetch_raindrop_bookmarks
from perplexity_generator import generate_ideas
from linkedin_poster import post_linkedin
from config import LAST_RUN_FILE
from datetime import datetime

def job():
    print(f"⏰ Running scheduled job at {datetime.now()}")
    bookmarks = fetch_raindrop_bookmarks(limit=5)
    for bm in bookmarks:
        content = generate_ideas(bm)
        if content:
            post_linkedin(content)
    with open(LAST_RUN_FILE, "w") as f:
        f.write(str(datetime.now()))

# Schedule posts: Tuesday & Friday at 10:00 AM
schedule.every().tuesday.at("10:00").do(job)
schedule.every().friday.at("10:00").do(job)

print("📅 Scheduler started. Waiting for next run...")

while True:
    schedule.run_pending()
    time.sleep(60)
