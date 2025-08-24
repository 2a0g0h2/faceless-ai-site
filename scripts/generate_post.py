import os
import json
import random
from datetime import datetime
from openai import OpenAI

# Nastavenie OpenAI klienta
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

POSTS_DIR = "posts"
IMAGES_DIR = "static/images"

topics = [
    "Artificial Intelligence in Daily Life",
    "Future of Renewable Energy",
    "Impact of Social Media on Society",
    "Space Exploration and Colonization",
    "Climate Change and Solutions",
    "Evolution of Technology in Education",
    "Healthcare Innovations with AI",
    "Cybersecurity in Modern World",
    "The Future of Remote Work",
    "Digital Art and Creativity"
]

def generate_article(topic):
    prompt = f"""
    Write a well-structured article of about 800 words on the topic: '{topic}'.
    The article should include:
    - An engaging introduction (2–3 paragraphs)
    - Several body sections with subheadings
    - A clear conclusion that wraps up the ideas
    - Natural paragraph flow like in a newspaper or magazine
    Use simple but professional language.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional journalist and article writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

def generate_image(topic):
    from openai import OpenAI
    # Tu môžeš neskôr nahradiť Unsplash API ak nechceš míňať kredity
    # Zatiaľ necháme fallback placeholder
    return "https://source.unsplash.com/800x400/?" + topic.replace(" ", ",")

def generate_post():
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)

    topic = random.choice(topics)
    article = generate_article(topic)

    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".json"
    filepath = os.path.join(POSTS_DIR, filename)

    image_url = generate_image(topic)

    # Vytvoríme krátky náhľad
    preview = article[:150].replace("\n", " ") + "..."

    post = {
        "title": topic,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "image": image_url,
        "preview": preview,
        "content": article
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=4)

    print(f"Generated post saved to {filepath}")

if __name__ == "__main__":
    generate_post()
