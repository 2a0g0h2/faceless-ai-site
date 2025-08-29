import os
import json
import random
from datetime import datetime
from openai import OpenAI

# Inicializácia OpenAI klienta
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Možné témy článkov
TOPICS = [
    "Top productivity hacks for remote workers",
    "The future of artificial intelligence in everyday life",
    "Best travel destinations for 2025",
    "Healthy lifestyle tips for busy professionals",
    "Latest trends in cryptocurrency and blockchain",
    "How to stay motivated while working from home",
    "The rise of electric vehicles and green energy",
    "Top 10 gadgets you need in 2025",
    "How social media is shaping our lives",
    "The psychology of habit building and self-discipline",
]

def generate_article(topic: str) -> str:
    """Vygeneruje článok na základe témy pomocou OpenAI API"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # lacnejší a rýchly model
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that writes engaging blog articles in markdown format.",
            },
            {"role": "user", "content": f"Write a blog article about: {topic}"},
        ],
        max_tokens=800,
    )

    return response.choices[0].message.content.strip()

def generate_post():
    """Hlavná funkcia na vytvorenie nového príspevku"""
    topic = random.choice(TOPICS)
    article = generate_article(topic)

    # pripraviť meta
    date = datetime.now().strftime("%Y-%m-%d")
    slug = topic.lower().replace(" ", "-")
    filename = f"posts/{date}-{slug}.json"

    # uisti sa že priečinok existuje
    os.makedirs("posts", exist_ok=True)

    post = {
        "title": topic,
        "date": date,
        "content": article,
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=2)

    print(f"✅ Generated post: {filename}")

if __name__ == "__main__":
    generate_post()
