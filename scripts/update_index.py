import os
from datetime import datetime

POSTS_DIR = "posts"
OUTPUT_FILE = "index.html"
IMAGES_DIR = "static/images"

def slug_to_title(slug: str) -> str:
    """Prevedie názov súboru na čitateľný titulok"""
    return slug.replace("-", " ").title()

def update_index():
    posts = []

    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".html"):
            slug = filename[:-5]  # bez .html
            title = slug_to_title(slug)
            path = os.path.join(POSTS_DIR, filename)

            # defaultný obrázok
            image_path = os.path.join(IMAGES_DIR, slug + ".jpg")
            if os.path.exists(image_path):
                image = image_path
            else:
                image = os.path.join(IMAGES_DIR, "default.png")

            posts.append({
                "title": title,
                "slug": slug,
                "image": image,
                "date": datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")
            })

    # zoradíme od najnovšieho
    posts.sort(key=lambda x: x["date"], reverse=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Faceless AI Blog</title></head><body>\n")
        f.write("<h1>Faceless AI Blog</h1>\n")
        for post in posts:
            f.write(f"""
            <div style="margin-bottom: 40px;">
                <h2><a href="posts/{post['slug']}.html">{post['title']}</a></h2>
                <img src="{post['image']}" alt="{post['title']}" style="max-width:600px;"><br>
                <small>{post['date']}</small>
            </div>
            """)
        f.write("</body></html>")

if __name__ == "__main__":
    update_index()
