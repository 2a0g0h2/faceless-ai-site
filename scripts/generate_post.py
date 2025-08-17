import os
import json
import random
from datetime import date
from faker import Faker

fake = Faker()

# Cesta do priečinka posts
posts_dir = "../posts/"
os.makedirs(posts_dir, exist_ok=True)

# Náhodné témy (možno rozšíriť)
topics = [
    "AI in Everyday Life",
    "Future of Remote Work",
    "Sustainable Technology",
    "Virtual Reality Trends",
    "Healthy Lifestyle Hacks",
    "Crypto Market Insights",
    "Digital Nomad Tips",
    "Top Productivity Tools",
    "Smart Home Innovations",
    "Gaming Industry Evolution"
]

# Generovanie náhodnej témy
topic = random.choice(topics)
today = date.today().isoformat()

# Generovanie textu článku
def generate_article():
    intro = f"{topic} is one of the hottest topics today. In this article, we explore key insights and trends you need to know."
    body = "\n\n".join([fake.paragraph(nb_sentences=5) for _ in range(5)])
    conclusion = "In conclusion, staying updated with these trends can help you adapt and thrive in the changing world."
    return intro, body, conclusion

intro, body, conclusion = generate_article()

# Generovanie cover image (placeholder)
cover_image = f"https://picsum.photos/seed/{random.randint(1,1000)}/800/400"

# Názov súboru
slug = topic.lower().replace(" ", "_")
base_path = os.path.join(posts_dir, slug)

# Ulož Markdown
with open(base_path + ".md", "w", encoding="utf-8") as f:
    f.write(f"# {topic}\n\n")
    f.write(f"![Cover Image]({cover_image})\n\n")
    f.write(f"{intro}\n\n{body}\n\n{conclusion}\n")

# Ulož HTML
with open(base_path + ".html", "w", encoding="utf-8") as f:
    f.write(f"<html><head><title>{topic}</title></head><body>\n")
    f.write(f"<h1>{topic}</h1>\n")
    f.write(f'<img src="{cover_image}" alt="Cover Image" style="max-width:100%;">\n')
    f.write(f"<p>{intro}</p>\n")
    f.write(f"<p>{body}</p>\n")
    f.write(f"<p>{conclusion}</p>\n")
    f.write("</body></html>")

# Ulož JSON (s date a excerpt)
excerpt = intro[:150] + "..."
with open(base_path + ".json", "w", encoding="utf-8") as f:
    json.dump({
        "title": topic,
        "intro": intro,
        "excerpt": excerpt,
        "image": cover_image,
        "date": today
    }, f, ensure_ascii=False, indent=2)

print(f"Generated post: {base_path}.md/.html/.json")
