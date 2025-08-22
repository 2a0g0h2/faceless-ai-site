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

        title = post.get("title", slug.replace(".html", "").replace("-", " ").title())
        date = post.get("date", "")
        image = post.get("image", "")
        content = post.get("content", "")

        # rozsekaj obsah na odseky podľa \n\n
        paragraphs = "".join(f"<p>{para.strip()}</p>" for para in content.split("\n\n") if para.strip())

        html_content = f"""<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <article class="post-container">
    <h1>{title}</h1>
    <p class="meta">{date}</p>
    {f'<img src="{image}" alt="{title}" onerror="this.onerror=null;this.src=\'images/default.svg\'">' if image else ''}
    {paragraphs or '<p></p>'}
    <p><a href="index.html">← Naspäť na domov</a></p>
  </article>
</body>
</html>
"""

        with open(page_path, "w", encoding="utf-8") as f:
            f.write(html_content)

    print("✅ HTML stránky článkov vygenerované do /docs")

if __name__ == "__main__":
    generate_pages()
