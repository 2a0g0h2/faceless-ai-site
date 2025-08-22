import json
import os

def generate_pages():
    os.makedirs("docs", exist_ok=True)
    for file in os.listdir("posts"):
        if file.endswith(".json"):
            with open(os.path.join("posts", file), "r", encoding="utf-8") as f:
                post = json.load(f)

            slug = file.replace(".json", ".html")
            page_path = os.path.join("docs", slug)

            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{post['title']}</title>
</head>
<body>
    <h1>{post['title']}</h1>
    <img src="{post['image']}" alt="{post['title']}" style="max-width:800px;">
    <p><em>Published on {post['date']}</em></p>
    {"".join([f"<p>{p}</p>" for p in post['content'].split("\\n\\n")])}
    <br><a href="index.html">← Back to home</a>
</body>
</html>"""

            with open(page_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            print(f"Generated page: {page_path}")

if __name__ == "__main__":
    generate_pages()
