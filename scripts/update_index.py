import os
import json
from datetime import datetime

POSTS_DIR = "posts"
OUTPUT_FILE = "index.html"

def update_index():
    posts = []

    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):  # berieme meta JSON
            filepath = os.path.join(POSTS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                post = json.load(f)

            posts.append({
                "title": post.get("title", "Untitled"),
                "slug": filename.replace(".json", ""),
                "image": post.get("image", ""),
                "date": post.get("date", datetime.today().strftime("%Y-%m-%d"))
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
