import os
import requests
import json
from datetime import datetime
import re
import random

# 🔑 API key z Pixabay (nastav v GitHub Secrets alebo .env)
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")

# ✨ Témy a ich titulky (rozšírené, aby mali rôznorodosť)
TOPICS = [
    ("blockchain", "How Blockchain is Transforming Human Experience"),
    ("artificial intelligence", "AI and the Future of Human Creativity"),
    ("virtual reality", "Exploring New Worlds in Virtual Reality"),
    ("sustainability", "Sustainability as the Core of Innovation"),
    ("cybersecurity", "Cybersecurity in the Age of AI"),
    ("space", "The Human Journey Into Space"),
    ("health", "Digital Health and the Future of Medicine"),
    ("education", "How Technology is Shaping Education"),
    ("metaverse", "Living in the Metaverse: Opportunities and Risks"),
    ("robotics", "Robotics and Human Collaboration")
]

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def fetch_pixabay_image(query):
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&image_type=photo&orientation=horizontal&per_page=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["hits"]:
            # vyber náhodný obrázok z 10 výsledkov
            return random.choice(data["hits"])["largeImageURL"]
    return None

def generate_post():
    topic, title = random.choice(TOPICS)
    slug = slugify(title)

    # 🖼️ stiahni obrázok z Pixabay
    image_url = fetch_pixabay_image(topic)
    if image_url:
        img_data = requests.get(image_url).content
        os.makedirs("public/images", exist_ok=True)
        image_path = f"public/images/{slug}.jpg"
        with open(image_path, "wb") as f:
            f.write(img_data)
        image_field = f"/images/{slug}.jpg"
    else:
        image_field = "/images/default.jpg"

    # 📝 JSON štruktúra
    post = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "title": title,
        "topic": topic,
        "image": image_field,
        "content": f"This article explores the topic of {topic}. More details will follow soon."
    }

    # 💾 uloženie do posts/
    os.makedirs("posts", exist_ok=True)
    with open(f"posts/{slug}.json", "w") as f:
        json.dump(post, f, indent=4)

    print(f"✅ Post generated: posts/{slug}.json with image {image_field}")

if __name__ == "__main__":
    generate_post()
