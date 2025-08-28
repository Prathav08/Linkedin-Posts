import requests
from config import PERPLEXITY_API_KEY, PERPLEXITY_MODEL

def generate_ideas(bookmark):
    prompt = (
        "Generate 5-7 highly creative and actionable LinkedIn post ideas "
        "based on this content. Each idea should include a catchy title and sub-headings for contents "
        "with steps or examples that make the idea practical and engaging. "
        "Keep it simple and easy to understand for anyone. "
        "Do not include hashtags or bold text. "
        "No References. "
        "Ensure no idea is repeated.\n"
        f"{bookmark['excerpt']}"
    )

    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": PERPLEXITY_MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": 0.7, "max_tokens": 40000}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    else:
        print(f"Perplexity API Error {response.status_code}: {response.text}")
        return ""
