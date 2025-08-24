import os
import json

POSTS_DIR = "posts"
INDEX_FILE = "index.html"

def update_index():
    posts = []
    for file in os.listdir(POSTS_DIR):
        if file.endswith(".json"):
            with open(os.path.join(POSTS_DIR, file), "r", encoding="utf-8") as f:
                posts.append(json.load(f))

    # sort by newest first
    posts.sort(key=lambda x: x["filename"], reverse=True)

    # build HTML for index
    html_posts = ""
    for post in posts:
        excerpt = post["content"].replace("<p>", "").replace("</p>", "")
        excerpt = excerpt.replace("<h2>", "").replace("</h2>", "")
        excerpt = excerpt.strip()[:250] + "..."  # 2–3 sentences

        html_posts += f"""
        <div class="post-preview">
            <h2>{post['title']}</h2>
            <img src="{post['image']}" alt="{post['title']}" style="max-width:400px;"><br>
            <p>{excerpt}</p>
            <a href="posts/{post['filename']}">Read more →</a>
        </div>
        <hr>
        """

    # final index.html
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Faceless AI Blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Faceless AI Blog</h1>
    {html_posts}
</body>
</html>
"""

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_html)

if __name__ == "__main__":
    update_index()
