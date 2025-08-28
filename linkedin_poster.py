import requests
from config import LINKEDIN_ACCESS_TOKEN, LINKEDIN_PAGE_URN

def post_linkedin(content):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}", "Content-Type": "application/json"}

    payload = {
        "author": LINKEDIN_PAGE_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("✅ LinkedIn post published!")
    else:
        print(f"❌ LinkedIn API Error {response.status_code}: {response.text}")
