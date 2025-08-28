import os

# API Tokens
RAINDROP_TOKEN = os.environ.get("RAINDROP_TOKEN")
PERPLEXITY_API_KEY = os.environ.get("PERPLEXITY_API_KEY")
LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

# Scheduler
POST_DAYS = ["Tuesday", "Friday"]  # Days to post
POST_HOUR = 9  # 9 AM Sydney time (best for engagement)
POST_MINUTE = 30

# Raindrop
RAINDROP_LIMIT = 5
