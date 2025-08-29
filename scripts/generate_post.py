import os
import json
import random
from datetime import datetime
from openai import OpenAI

client = OpenAI()

# model sa dá nastaviť v GitHub Actions (default gpt-4o-mini)
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# tvoje fixné témy (napr. zaujímavé oblasti, ktoré chceš pravidelne pokrývať)
FIXED_TOPICS = [
    "The future of electric cars",
    "Top productivity hacks for remote workers",
    "Healthy eating on a budget",
    "Best practices for personal finance in 2025",
    "The psychology of social media use",
]

def get_trending_topics():
    """Získa témy podľa trendov (GPT vygeneruje nové návrhy)."""
    prompt = """
    Generate 10 trending article topics for a blog. 
    Mix technology, lifestyle, health, entertainment, travel, finance, and culture. 
    Return them as a simple JSON list of strings.
    """
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a trend researcher."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
    )
    
    try:
        topics = json.loads(response.choices[0].message.content.strip())
    except Exception:
        topics = ["AI trends in 2025", "Healthy morning routines", "Top travel destinations"]
    
    return topics

def generate_article(topic):
    """Vygeneruje článok na danú tému."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a professional blog writer."},
            {"role": "user", "content": f"Write a detailed SEO-friendly blog article about: {topic}. Length: ~800 words."}
        ],
        max_tokens=1200,
    )
    return response.choices[0].message.content

def generate_post():
    # získa trendy témy
    trending = get_trending_topics()
    # spojíme s fixnými
    topics = trending + FIXED_TOPICS
    topic = random.choice(topics)

    article = generate_article(topic)

    post = {
        "title": topic,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "content": article
    }

    filename = f"content/posts/{datetime.now().strftime('%Y-%m-%d')}-{topic.replace(' ', '-')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=2)

    print(f"✅ Generated post saved to {filename}")

if __name__ == "__main__":
    generate_post()
