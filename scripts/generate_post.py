import os
import json
import random
from datetime import datetime
from openai import OpenAI

# Inicializácia OpenAI klienta
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Definované témy článkov (rôzne trendy + všeobecné kategórie)
TOPICS = [
    "Top productivity hacks for remote workers",
    "Latest trends in AI and machine learning",
    "How to stay fit while working from home",
    "The future of electric cars",
    "Best budget travel destinations 2025",
    "Top 10 healthy recipes for busy people",
    "How to build passive income online",
    "Latest social media marketing strategies",
    "Best personal finance tips for 2025",
    "How to learn coding fast as a beginner",
    "Top gadgets every tech lover needs",
    "How to improve your sleep quality",
    "Best books to read in 2025",
    "Guide to starting a successful side hustle",
    "Top 5 movies everyone should watch this year"
]

def generate_article(topic: str) -> str:
    """Vygeneruje článok na základe témy pomocou GPT-4o-mini."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes engaging blog posts."},
            {"role": "user", "content": f"Write a 600-word blog post about: {topic}. Make it informative, engaging, and well-structured with clear sections."}
        ],
        temperature=0.7,
        max_tokens=1000,
    )
    return response.choices[0].message.content.strip()

def generate_post():
    """Hlavná funkcia – vyberie tému, vygeneruje článok a uloží ho do posts/"""
    # Vyber náhodnú tému
    topic = random.choice(TOPICS)
    print(f"Generating article for topic: {topic}")

    # Vygeneruj článok
    article = generate_article(topic)

    # Priprav názov súboru
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = topic.lower().replace(" ", "-").replace("?", "").replace(",", "").replace(".", "")
    filename = f"posts/{date_str}-{slug}.json"

    # Uisti sa, že priečinok existuje
    os.makedirs("posts", exist_ok=True)

    # Ulož JSON
    post_data = {
        "title": topic,
        "date": date_str,
        "content": article
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post_data, f, indent=2, ensure_ascii=False)

    print(f"Post saved to {filename}")

if __name__ == "__main__":
    generate_post()
