import schedule
import time
from datetime import datetime
from raindrop_fetcher import fetch_raindrop_bookmarks
from idea_generator import generate_ideas
from linkedin_poster import post_to_linkedin
import pytz

def job():
    sydney_tz = pytz.timezone("Australia/Sydney")
    now = datetime.now(sydney_tz)
    print(f"Running LinkedIn post job at {now}")
    
    bookmarks = fetch_raindrop_bookmarks()
    if not bookmarks:
        print("No new bookmarks.")
        return
    
    for bm in bookmarks:
        post_content = generate_ideas(bm)
        if post_content:
            post_to_linkedin(post_content)

# Scheduler for Tuesday and Friday
schedule.every().tuesday.at("09:30").do(job)
schedule.every().friday.at("09:30").do(job)

print("Scheduler started. Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(30)
