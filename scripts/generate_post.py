import os
import random
import datetime
import requests

POSTS_DIR = "../posts"
TEMPLATE_FILE = "../templates/post_template.html"

# Témy, z ktorých sa náhodne vyberie
TOPICS = [
    "Future of Artificial Intelligence",
    "Neural Networks and Deep Learning",
    "AI and Human Creativity",
    "Virtual Reality and Society",
    "Ethics of Artificial Intelligence",
    "Technology and the Future of Work",
]

UNSPLASH_TAGS = ["ai", "future", "technology", "cyber", "robot", "innovation"]

def generate_paragraph(topic):
    """Vytvorí odsek cca 120-150 slov"""
    sentences = [
        f"{topic} is changing the way we live and work every single day.",
        "This transformation comes with opportunities but also major challenges.",
        "Experts suggest that the next decade will define how society adapts.",
        "Innovations are being developed faster than regulations can keep up.",
        "Ethics, responsibility, and creativity play a huge role in this process.",
        "Some see AI as a tool, while others fear it could surpass human control.",
    ]
    text = " ".join(random.sample(sentences, 5))
    return f"<p>{text}</p>"

def generate_image():
    tag = random.choice(UNSPLASH_TAGS)
    return f'<img src="https://source.unsplash.com/800x400/?{tag}" alt="{tag}">'

def generate_post():
    topic = random.choice(TOPICS)
    title = f"{topic} - {datetime.date.today().strftime('%B %d, %Y')}"
    date = datetime.date.today().strftime("%B %d, %Y")

    paragraphs = []
    for i in range(random.randint(6, 8)):
        paragraphs.append(f"<h2>{topic} - Part {i+1}</h2>")
        paragraphs.append(generate_paragraph(topic))
        if i % 2 == 0:  # každé 2 odseky daj obrázok
            paragraphs.append(generate_image())

    content = "\n".join(paragraphs)

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    html = template.replace("{{title}}", title).replace("{{date}}", date).replace("{{content}}", content)

    filename = f"{datetime.date.today().strftime('%Y-%m-%d')}.html"
    filepath = os.path.join(POSTS_DIR, filename)

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Post generated: {filepath}")

if __name__ == "__main__":
    generate_post()
