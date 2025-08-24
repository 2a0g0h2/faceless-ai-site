import os
import json

POSTS_DIR = "posts"
INDEX_FILE = "index.html"

def update_index():
    posts = []

    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(POSTS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                post = json.load(f)
                post["filename"] = filename.replace(".json", ".html")
                posts.append(post)

    # zoradíme podľa dátumu (novšie hore)
    posts.sort(key=lambda x: x["date"], reverse=True)

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Faceless AI Blog</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #000;
            color: #fff;
            line-height: 1.6;
            max-width: 1000px;
            margin: auto;
            padding: 20px;
        }}
        .post {{
            border-bottom: 1px solid #333;
            padding: 20px 0;
        }}
        .post img {{
            max-width: 100%;
            border-radius: 10px;
        }}
        a {{
            color: #1e90ff;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>Faceless AI Blog</h1>
"""

    for post in posts:
        html_content += f"""
    <div class="post">
        <h2><a href="pages/{post['filename']}">{post['title']}</a></h2>
        <p><em>{post['date']}</em></p>
        <img src="{post['image']}" alt="{post['title']}">
        <p>{post['preview']} <a href="pages/{post['filename']}">Read more</a></p>
    </div>
"""

    html_content += """
</body>
</html>"""

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Updated {INDEX_FILE}")

if __name__ == "__main__":
    update_index()
