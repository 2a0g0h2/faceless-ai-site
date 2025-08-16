import random
import requests
import re

UNSPLASH_ACCESS_KEY = "6WT8TnP8wBB3rBA43R3WHkb3P_awqh4tp0prBsG6An"

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def get_trending_topic():
    # Simple list of trending placeholder topics (can be expanded)
    topics = [
        "Artificial Intelligence", "Climate Change", "Space Exploration",
        "Quantum Computing", "Cybersecurity", "Health Tech",
        "Global Economy", "Virtual Reality", "Green Energy", "Future of Work"
    ]
    return random.choice(topics)

def get_unsplash_image_url(query):
    url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return data.get("urls", {}).get("regular", "")
    except Exception:
        pass
    return ""
