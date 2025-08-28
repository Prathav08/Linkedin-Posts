import requests
from config import PERPLEXITY_API_KEY

def generate_ideas(bookmark):
    prompt = (
        "Generate 1 highly creative and actionable LinkedIn post "
        "based on this content. Include a catchy title, step-by-step points, "
        "examples, and make it engaging for LinkedIn.\n\n"
        f"{bookmark['excerpt']}"
    )

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 2000
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    else:
        print(f"Perplexity API Error {response.status_code}: {response.text}")
        return ""
