import os
import uuid
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

POSTS_DIR = Path("posts")
IMAGES_DIR = POSTS_DIR / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def generate_image(title: str):
    filename = f"{uuid.uuid4().hex}.png"
    path = IMAGES_DIR / filename

    img = Image.new("RGB", (800, 400), color=(30, 30, 30))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((20, 180), title, fill=(102, 179, 255), font=font)
    img.save(path)
    return f"images/{filename}"

def generate_post():
    title = f"AI Post {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"
    content = f"This is an AI-generated post titled **{title}**.\n\nLorem ipsum content here."
    image_path = generate_image(title)
    
    filename = POSTS_DIR / f"{uuid.uuid4().hex}.md"
    with open(filename, "w") as f:
        f.write(f"---\ntitle: {title}\ndate: {datetime.utcnow()}\nimage: {image_path}\n---\n\n{content}")

if __name__ == "__main__":
    generate_post()
