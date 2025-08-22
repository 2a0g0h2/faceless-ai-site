import json
import os
import random
from datetime import datetime
import requests

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")

topics = [
    "artificial intelligence",
    "blockchain",
    "virtual reality",
    "metaverse",
    "quantum computing",
    "cybersecurity",
    "digital identity",
    "space exploration",
    "green energy",
    "future of work"
]

def fetch_pixabay_image(query):
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&image_type=photo&orientation=horizontal&per_page=10"
    response = requests.get(url)
    data = response.json()
    if "hits" in data and data["hits"]:
        return random.choice(data["hits"])["webformatURL"]
    return "https://via.placeholder.com/600x400?text=No+Image"

def generate_content(topic):
    """Generate ~800 words of placeholder content in paragraphs"""
    paragraphs = []
    for i in range(8):  # ~100 words per paragraph
        paragraph = (
            f"{topic.title()} is shaping the modern world in unexpected ways. "
            f"In this section, we explore perspective {i+1}, reflecting on how "
            f"technological, social, and ethical questions are influenced by {topic}. "
            f"The discussion emphasizes challenges, opportunities, and future outlooks."
        )
        paragraphs.append(paragraph)
    return "\n\n".join(paragraphs)

def main():
    topic = random.choice(topics)
    title = f"How {topic.title()} is Transforming Human Experience"
    date = datetime.now().strftime("%Y-%m-%d")
    image_url = fetch_pixabay_image(topic)

    post = {
        "date": date,
        "title": title,
        "topic": topic,
        "image": image_url,
        "content": generate_content(topic)
    }

    os.makedirs("posts", exist_ok=True)
    filename = f"posts/{date}-{topic.replace(' ', '_')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=4)

    print(f"Generated post saved as {filename}")

if __name__ == "__main__":
    main()
