import os
import uuid
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

POSTS_DIR = "posts"
IMAGES_DIR = "images"

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

def generate_unique_image(filename):
    # Vytvorí jednoduchý unikátny obrázok (placeholder)
    img = Image.new('RGB', (800, 400), color=(255, 200, 200))
    d = ImageDraw.Draw(img)
    d.text((10, 10), f"Article {filename}", fill=(0, 0, 0))
    img.save(os.path.join(IMAGES_DIR, filename + ".png"))

def generate_post():
    uid = str(uuid.uuid4())[:8]
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    title = f"AI Generated Article {uid}"
    filename = f"{date_str}_{uid}.html"

    # Generovanie unikátneho obrázku
    generate_unique_image(uid)

    content = f"""
    <html>
        <head><title>{title}</title></head>
        <body>
            <h1>{title}</h1>
            <img src="../{IMAGES_DIR}/{uid}.png" alt="{title}">
            <p>This is an AI generated post created on {date_str}.</p>
        </body>
    </html>
    """

    with open(os.path.join(POSTS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Generated post: {filename}")

if __name__ == "__main__":
    generate_post()

