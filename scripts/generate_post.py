import os
import json
import requests
from datetime import datetime
import random

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")
POSTS_DIR = "posts"

TOPICS = [
    ("The Future of Artificial Intelligence", "ai"),
    ("How Blockchain is Transforming Human Experience", "blockchain"),
    ("The Rise of Quantum Computing", "quantum"),
    ("Exploring the Metaverse", "metaverse"),
    ("Ethics in AI Development", "ethics"),
]

def get_pixabay_image(query):
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&image_type=photo&orientation=horizontal&per_page=50"
    response = requests.get(url)
    data = response.json()

    if "hits" in data and len(data["hits"]) > 0:
        return random.choice(data["hits"])["webformatURL"]

    return ""

def generate_post():
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)

    # vyber náhodnú tému
    title, topic = random.choice(TOPICS)
    slug = title.lower().replace(" ", "_").replace("/", "_")
    date = datetime.today().strftime("%Y-%m-%d")

    # obrázok z Pixabay
    image_url = get_pixabay_image(topic)

    # obsah článku
    content = f"This article explores the topic of {topic}. More details will follow soon."

    # HTML verzia článku
    html_file = os.path.join(POSTS_DIR, f"{slug}.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(f"<html><head><title>{title}</title></head><body>")
        f.write(f"<h1>{title}</h1>")
        if image_url:
            f.write(f'<img src="{image_url}" alt="{title}" style="max-width:600px;"><br>')
        f.write(f"<p>{content}</p>")
        f.write("</body></html>")

    # JSON meta súbor
    meta = {
        "date": date,
        "title": title,
        "topic": topic,
        "image": image_url,
        "content": content,
    }
    json_file = os.path.join(POSTS_DIR, f"{slug}.json")
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=4)

    print(f"✅ Post generated: {title}")

if __name__ == "__main__":
    generate_post()
