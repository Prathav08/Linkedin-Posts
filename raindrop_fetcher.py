import requests
from datetime import datetime, timedelta, timezone
from config import RAINDROP_TOKEN

def fetch_raindrop_bookmarks(limit=10, days=5):
    """Fetch bookmarks from last `days` days"""
    now = datetime.now(timezone.utc)
    cutoff_ts = (now - timedelta(days=days)).timestamp()

    headers = {"Authorization": f"Bearer {RAINDROP_TOKEN}"}
    response = requests.get(f"https://api.raindrop.io/rest/v1/raindrops/0?perpage={limit}", headers=headers)
    response.raise_for_status()

    items = response.json().get("items", [])
    recent = []
    for item in items:
        created_str = item.get("created", "")
        try:
            created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
            if created_dt.timestamp() >= cutoff_ts:
                recent.append({"excerpt": item.get("excerpt", "")})
        except Exception:
            continue
    return recent
