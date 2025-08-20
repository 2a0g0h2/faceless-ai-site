import os
import requests
import json
import random
from datetime import datetime

# Pixabay API kľúč – nastav vo svojom GitHub repozitári ako secret (napr. PIXABAY_API_KEY)
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")

# Témy článkov
TOPICS = [
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "neural networks",
    "robotics",
    "cybersecurity",
    "blockchain",
    "virtual reality",
    "augmented reality",
    "quantum computing"
]

# Funkcia na generovanie rozšírených titulkov
def generate_title_from_topic(topic):
    templates = [
        f"Exploring the Role of {topic.title()} in the Age of AI",
        f"The Future of {topic.title()} and Its Impact on Society",
        f"How {topic.title()} is Transforming Human Experience",
        f"Understanding the Importance of {topic.title()} in Modern Technology",
        f"{topic.title()} and the Challenges of Tomorrow",
    ]
    return random.choice(templates)

# Funkcia na získanie obrázka z Pixabay
def fetch_pixabay_image(topic):
    url = "https://pixabay.com/api/"
    params = {
        "key": PIXABAY_API_KEY,
        "q": topic,
        "image_type": "photo",
        "orientation": "horizontal",
        "safesearch": "true",
        "per_page": 50
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "hits" in data and len(data["hits"]) > 0:
            return random.choice(data["hits"])["webformatURL"]
        else:
            return "https://via.placeholder.com/800x400?text=No+Image+Found"
    else:
        raise Exception(f"Nepodarilo sa načítať obrázok z Pixabay: {response.status_code}")

def generate_post():
    topic = random.choice(TOPICS)
    title = generate_title_from_topic(topic)
    image_url = fetch_pixabay_image(topic)

    today = datetime.utcnow().strftime("%Y-%m-%d")

    post = {
        "date": today,
        "title": title,
        "topic": topic,
        "image": image_url,
        "content": f"This article explores the topic of {topic}. More details will follow soon."
    }

    os.makedirs("posts", exist_ok=True)
    filename = f"posts/{today}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=4)

    print(f"✅ Post generated: {filename}")

if __name__ == "__main__":
    generate_post()
