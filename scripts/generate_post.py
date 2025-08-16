import os
import json
from datetime import datetime
import random

# Tu môžeš pridať viac tém podľa trendov
TOPICS = [
    "AI in Healthcare",
    "Future of Electric Vehicles",
    "Space Tourism",
    "Neuroscience Breakthroughs",
    "Sustainable Fashion",
    "Quantum Computing Trends",
    "Virtual Reality in Education",
    "Green Energy Innovations",
    "Cryptocurrency Regulation",
    "Smart Home Technology"
]

# Funkcia na generovanie textu článku
def generate_article(topic):
    intro = f"Explore the latest insights on {topic}. This article covers key developments and their impact in 2025."
    body = "\n\n".join([f"Section {i+1}: Lorem ipsum dolor sit amet, consectetur adipiscing elit." for i in range(random.randint(3,6))])
    conclusion = f"In conclusion, {topic} continues to shape the industry, offering new opportunities and challenges."
    return intro, body, conclusion

# Funkcia na generovanie cover image URL (placeholder)
def generate_cover_image(topic):
    # Použijeme náhodný obrázok z placeholder API
    width = 1200
    height = 600
    return f"https://picsum.photos/seed/{topic.replace(' ','_')}/{width}/{height}"

def main():
    # Vyber náhodnú tému
    topic = random.choice(TOPICS)
    
    # Generuj článok
    intro, body, conclusion = generate_article(topic)
    cover_image = generate_cover_image(topic)
    today = datetime.utcnow().strftime("%Y-%m-%d")
    
    # Priprav názvy súborov
    safe_title = topic.lower().replace(" ", "-")
    base_path = os.path.join("posts", f"{today}-{safe_title}")
    
    # Ulož Markdown
    with open(base_path + ".md", "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n![Cover]({cover_image})\n\n{intro}\n\n{body}\n\n{conclusion}")
    
    # Ulož HTML
    with open(base_path + ".html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic}</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>
<article>
<h1>{topic}</h1>
<img src="{cover_image}" alt="{topic} cover" class="cover-image">
<p>{intro}</p>
<p>{body}</p>
<p>{conclusion}</p>
</article>
</body>
</html>""")
    
    # Ulož JSON
    with open(base_path + ".json", "w", encoding="utf-8") as f:
        json.dump({
            "title": topic,
            "intro": intro,
            "image": cover_image,
            "date": today  # Dôležité pre update_index.py
        }, f, ensure_ascii=False, indent=2)
    
    print(f"Generated article: {base_path}.md/.html/.json")

if __name__ == "__main__":
    main()

