import requests
from datetime import datetime, timedelta, timezone
from config import RAINDROP_TOKEN, RAINDROP_LIMIT

def fetch_raindrop_bookmarks():
    now = datetime.now(timezone.utc)
    five_days_ago_ts = (now - timedelta(days=5)).timestamp()
    headers = {"Authorization": f"Bearer {RAINDROP_TOKEN}"}
    response = requests.get(f"https://api.raindrop.io/rest/v1/raindrops/0?perpage={RAINDROP_LIMIT}", headers=headers)
    response.raise_for_status()
    items = response.json().get("items", [])

    recent_bookmarks = []
    for item in items:
        created_str = item.get("created", "")
        try:
            created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
            if created_dt.timestamp() >= five_days_ago_ts:
                recent_bookmarks.append({"excerpt": item.get("excerpt", "")})
        except Exception:
            continue
    return recent_bookmarks
