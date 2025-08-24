import os
import json

POSTS_DIR = "posts"
PAGES_DIR = "pages"

def generate_pages():
    os.makedirs(PAGES_DIR, exist_ok=True)

    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(POSTS_DIR, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                post = json.load(f)

            page_filename = filename.replace(".json", ".html")
            page_path = os.path.join(PAGES_DIR, page_filename)

            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{post['title']}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #000;
            color: #fff;
            line-height: 1.6;
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }}
        h1 {{
            margin-bottom: 20px;
        }}
        img {{
            max-width: 100%;
            border-radius: 10px;
            margin-bottom: 20px;
        }}
        p {{
            margin-bottom: 16px;
        }}
    </style>
</head>
<body>
    <h1>{post['title']}</h1>
    <p><em>{post['date']}</em></p>
    <img src="{post['image']}" alt="{post['title']}">
    {"".join(f"<p>{para}</p>" for para in post['content'].split("\\n") if para.strip())}
</body>
</html>"""

            with open(page_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            print(f"Generated page: {page_path}")

if __name__ == "__main__":
    generate_pages()
