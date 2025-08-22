import os
import json
import random
import requests
from datetime import datetime
import textwrap

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")

TOPICS = [
    "artificial intelligence",
    "blockchain",
    "virtual reality",
    "quantum computing",
    "sustainability",
    "space exploration",
    "biotechnology",
    "cybersecurity",
    "robotics",
    "future of work"
]

def generate_long_content(topic: str) -> str:
    # jednoduchý text pre 800+ slov (môžeš neskôr nahradiť GPT volaním)
    paragraph = (
        f"{topic.capitalize()} is one of the most fascinating fields of our time. "
        "It influences society, economics, and the way humans interact with technology. "
        "In this article, we will explore its history, current state, and potential future impact. "
    )
    text = " ".join([paragraph] * 50)  # cca 800+ slov
    wrapped = "\n\n".join(textwrap.wrap(text, width=100))
    return wrapped

def fetch_image(topic: str) -> str:
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={topic}&image_type=photo&per_page=10"
    r = requests.get(url)
    data = r.json()
    hits = data.get("hits", [])
    if not hits:
        return None
    img_url = hits[0]["webformatURL"]

    os.makedirs("images", exist_ok=True)
    img_path = f"images/{topic.replace(' ', '_')}.jpg"

    img_data = requests.get(img_url).content
    with open(img_path, "wb") as f:
        f.write(img_data)

    return img_path

def main():
    topic = random.choice(TOPICS)
    today = datetime.today().strftime("%Y-%m-%d")

    title = f"How {topic.title()} is Changing Our World"
    filename = f"posts/{today}-{topic.replace(' ', '_')}.json"

    os.makedirs("posts", exist_ok=True)

    image_path = fetch_image(topic)

    post = {
        "date": today,
        "title": title,
        "topic": topic,
        "image": image_path,
        "content": generate_long_content(topic)
    }

    with open(filename, "w") as f:
        json.dump(post, f, indent=4)

if __name__ == "__main__":
    main()
