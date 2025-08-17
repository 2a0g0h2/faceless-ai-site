import os
import datetime
import requests
import json
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "posts"
IMAGES_DIR = Path(__file__).parent.parent / "images"

# Vytvorenie adresárov ak neexistujú
POSTS_DIR.mkdir(exist_ok=True)
IMAGES_DIR.mkdir(exist_ok=True)

def generate_ai_content():
    # Tu bude volanie AI generátora obsahu
    # Príklad štruktúry článku
    title = "AI Generated Post " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    content = "Toto je automaticky generovaný článok AI. " * 20
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    return title, content, date

def generate_ai_image():
    # Tu bude volanie AI generátora obrázku (napr. Unsplash API alebo iný)
    # Pre test použijeme placeholder
    image_url = "https://source.unsplash.com/800x600/?technology"
    response = requests.get(image_url)
    image_name = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    image_path = IMAGES_DIR / image_name
    with open(image_path, "wb") as f:
        f.write(response.content)
    return f"../images/{image_name}"

def create_post_file(title, content, date, image_path):
    slug = title.lower().replace(" ", "-")
    post_file = POSTS_DIR / f"{slug}.html"
    html_content = f"""<div class="post-container">
<h1>{title}</h1>
<p class="meta">{date}</p>
<img src="{image_path}" alt="{title}">
<p>{content}</p>
</div>"""
    with open(post_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Post created: {post_file}")

def main():
    title, content, date = generate_ai_content()
    image_path = generate_ai_image()
    create_post_file(title, content, date, image_path)

if __name__ == "__main__":
    main()
