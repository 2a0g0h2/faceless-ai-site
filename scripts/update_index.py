import os
from pathlib import Path
import frontmatter

POSTS_DIR = Path("posts")
INDEX_FILE = Path("index.html")

posts = []
for file in sorted(POSTS_DIR.glob("*.md"), reverse=True):
    if file.name == "images":
        continue
    post = frontmatter.load(file)
    posts.append({
        "title": post["title"],
        "image": post.get("image", ""),
        "filename": file.name
    })

html_posts = ""
for post in posts:
    html_posts += f"""
    <div class="post-card">
        <a href="posts/{post['filename'].replace('.md', '.html')}">
            <img src="{post['image']}" alt="{post['title']}">
            <div class="post-card-content">
                <h2>{post['title']}</h2>
            </div>
        </a>
    </div>
    """

INDEX_HTML = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Faceless AI Site</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
    <div class="posts-grid">
        {html_posts}
    </div>
</div>
</body>
</html>
"""

with open(INDEX_FILE, "w") as f:
    f.write(INDEX_HTML)
