import os
import json

POSTS_DIR = "posts"
DOCS_DIR = "docs"

def generate_pages():
    os.makedirs(DOCS_DIR, exist_ok=True)

    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            post = json.load(f)

        slug = filename.replace(".json", ".html")
        page_path = os.path.join(DOCS_DIR, slug)

        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post['title']}</title>
</head>
<body>
    <h1>{post['title']}</h1>
    <p><em>{post['date']}</em></p>
    <img src="{post['image']}" alt="{post['title']}" style="max-width:600px;"><br><br>
    {"".join(f"<p>{paragraph}</p>" for paragraph in post['content'].split("\\n\\n"))}
    <br><br>
    <a href="index.html">← Back to home</a>
</body>
</html>
"""

        with open(page_path, "w", encoding="utf-8") as f:
            f.write(html_content)

if __name__ == "__main__":
    generate_pages()
