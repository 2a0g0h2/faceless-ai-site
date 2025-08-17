import os
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "posts"
INDEX_FILE = Path(__file__).parent.parent / "index.html"

def update_index():
    POSTS_DIR.mkdir(exist_ok=True)
    posts_html = []

    for f in sorted(POSTS_DIR.iterdir(), reverse=True):
        if f.suffix == ".html":
            with open(f, "r", encoding="utf-8") as file:
                html = file.read()
                # Bezpečne extrahovanie dátumu a nadpisu
                date = html.split('<p class="meta">')[1].split("</p>")[0] if '<p class="meta">' in html else "N/A"
                title = html.split("<h1>")[1].split("</h1>")[0] if "<h1>" in html else "Untitled"
                img_tag = ""
                if "<img " in html:
                    img_tag = html.split("<img ")[1].split(">")[0]
                    img_tag = "<img " + img_tag + ">"
                posts_html.append(f"""
<div class="post-card">
    {img_tag}
    <div class="post-card-content">
        <h2>{title}</h2>
        <p>{date}</p>
    </div>
</div>
""")

    index_content = f"""<html>
<head>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
<div class="posts-grid">
{''.join(posts_html)}
</div>
</div>
</body>
</html>"""

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"Index updated: {INDEX_FILE}")

if __name__ == "__main__":
    update_index()
