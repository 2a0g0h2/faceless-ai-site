import os
import random
from datetime import datetime

POSTS_DIR = "../posts"
IMAGES_DIR = "../images"

def get_random_image():
    imgs = [f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    if not imgs:
        return None
    return f"images/{random.choice(imgs)}"

def generate_post():
    title = f"Awesome Post {random.randint(1,1000)}"
    excerpt = "This is a short excerpt of the article."
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cover_image = get_random_image() or "images/default.jpg"

    filename = f"{POSTS_DIR}/{title.replace(' ', '_')}.html"
    content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="post-container">
    <h1>{title}</h1>
    <img src="{cover_image}" alt="{title}" class="cover-image">
    <p>{excerpt}</p>
    <p>Full content goes here. Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
</div>
</body>
</html>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")

def main():
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)
    generate_post()

if __name__ == "__main__":
    main()

