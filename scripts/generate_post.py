import os
import datetime
import random

POSTS_DIR = "../posts"
IMAGES_DIR = "../images"

if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

def generate_unique_filename(prefix="post", ext="html"):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    rand = random.randint(1000, 9999)
    return f"{prefix}_{timestamp}_{rand}.{ext}"

def generate_post_content(title, image_filename):
    # Obsah článku – nadpisy, odstavce
    content = f"""
    <div class="post-container">
        <h1>{title}</h1>
        <p class="meta">{datetime.datetime.now().strftime("%d.%m.%Y")}</p>
        <img src="../images/{image_filename}" alt="{title}">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet...</p>
        <h2>Podnadpis 1</h2>
        <p>Viac textu, príklady a vysvetlenia...</p>
        <h2>Podnadpis 2</h2>
        <p>Ďalší obsah článku, zaujímavé info...</p>
    </div>
    """
    return content

def generate_post():
    title = f"Automaticky generovaný článok {random.randint(100,999)}"
    html_filename = generate_unique_filename()
    image_filename = generate_unique_filename(prefix="img", ext="png")
    
    # Vytvor prázdny obrázok ako placeholder
    from PIL import Image
    img = Image.new("RGB", (800, 400), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    img.save(os.path.join(IMAGES_DIR, image_filename))

    content = generate_post_content(title, image_filename)
    
    with open(os.path.join(POSTS_DIR, html_filename), "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Post {title} vygenerovaný: {html_filename}")

if __name__ == "__main__":
    generate_post()
