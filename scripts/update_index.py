import os
import json
from datetime import datetime

POSTS_DIR = "posts"
INDEX_FILE = "index.html"

def generate_slug(title):
    return title.lower().replace(" ", "-").replace("?", "").replace("!", "").replace(".", "")

def update_index():
    # načítame všetky JSON súbory z posts
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(POSTS_DIR, filename), "r") as f:
                post = json.load(f)
                slug = generate_slug(post['title'])
                posts.append((post, slug))

    # zoradíme články podľa dátumu (najnovšie hore)
    posts.sort(key=lambda x: x[0]["date"], reverse=True)

    # vygenerujeme obsah index.html
    post_entries = ""
    for post, slug in posts:
        image_html = f'<img src="{post.get("image", "https://via.placeholder.com/600x400")}" alt="{post["title"]}" style="max-width:600px;"><br>'
        
        post_entry = f"""
        <div style="margin-bottom:40px;">
            <a href="posts/{slug}.html" style="text-decoration:none; color:inherit;">
                {image_html}
                <h2>{post['title']}</h2>
            </a>
            <p>{post.get('content', '')}</p>
        </div>
        """
        post_entries += post_entry

    # kompletný HTML súbor
    index_content = f"""
    <html>
    <head>
        <title>Faceless AI Blog</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>Faceless AI Blog</h1>
        {post_entries}
    </body>
    </html>
    """

    with open(INDEX_FILE, "w") as f:
        f.write(index_content)

if __name__ == "__main__":
    update_index()
