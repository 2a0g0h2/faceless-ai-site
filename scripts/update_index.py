import os
import json
from datetime import datetime

POSTS_DIR = "posts"
DOCS_DIR = "docs"
IMAGES_SUBDIR = "images"                      # relatívne voči DOCS_DIR
INDEX_FILE = os.path.join(DOCS_DIR, "index.html")


def ensure_dirs_and_placeholder():
    os.makedirs(DOCS_DIR, exist_ok=True)
    images_dir = os.path.join(DOCS_DIR, IMAGES_SUBDIR)
    os.makedirs(images_dir, exist_ok=True)

    # Vytvor minimalistický SVG placeholder, ak chýba
    placeholder_path = os.path.join(images_dir, "default.svg")
    if not os.path.isfile(placeholder_path):
        svg = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500">
  <rect width="100%" height="100%" fill="#1e1e1e"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
        font-family="Inter, Roboto, sans-serif" font-size="28" fill="#888">
    No image
  </text>
</svg>"""
        with open(placeholder_path, "w", encoding="utf-8") as f:
            f.write(svg)


def safe_date(d: str, fallback_ts: float) -> datetime:
    # Skús ISO (YYYY-MM-DD), inak použij mtime súboru
    try:
        return datetime.fromisoformat(d)
    except Exception:
        return datetime.fromtimestamp(fallback_ts)


def make_excerpt(text: str, words: int = 28) -> str:
    # zober prvých ~N slov
    tokens = (text or "").split()
    if len(tokens) <= words:
        return " ".join(tokens)
    return " ".join(tokens[:words]) + "…"


def load_posts():
    posts_meta = []
    if not os.path.isdir(POSTS_DIR):
        return posts_meta

    for fname in os.listdir(POSTS_DIR):
        if not fname.endswith(".json"):
            continue

        fpath = os.path.join(POSTS_DIR, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            # ak by bol pokazený JSON, preskoč
            continue

        slug = os.path.splitext(fname)[0]          # napr. '2025-08-20-ai-a-zivot'
        page = f"{slug}.html"
        # pole 'image' v JSON je typicky "images/<slug>.jpg" (relatívne k docs/)
        image_rel = data.get("image") or f"{IMAGES_SUBDIR}/{slug}.jpg"

        # Over, či obrázok existuje v docs; ak nie, fallback na default.svg
        image_path_in_docs = os.path.join(DOCS_DIR, image_rel)
        if not os.path.isfile(image_path_in_docs):
            image_rel = f"{IMAGES_SUBDIR}/default.svg"

        title = data.get("title") or slug.replace("-", " ").title()
        date_str = data.get("date") or ""
        content = data.get("content") or ""
        excerpt = data.get("excerpt") or make_excerpt(content, 28)

        mtime = os.path.getmtime(fpath)
        sort_dt = safe_date(date_str, mtime)

        posts_meta.append({
            "slug": slug,
            "page": page,
            "title": title,
            "date": date_str if date_str else sort_dt.strftime("%Y-%m-%d"),
            "image": image_rel,
            "excerpt": excerpt,
            "sort_dt": sort_dt,
        })

    # Najnovšie hore
    posts_meta.sort(key=lambda x: x["sort_dt"], reverse=True)
    return posts_meta


def build_index_html(posts):
    # index sa spolieha na tvoj existujúci style.css v /docs
    cards_html = []
    for p in posts:
        cards_html.append(
            f"""
            <article class="post-card">
              <a href="{p['page']}">
                <img src="{p['image']}" alt="{p['title']}" onerror="this.onerror=null;this.src='images/default.svg'">
                <div class="post-card-content">
                  <h2>{p['title']}</h2>
                  <p class="meta">{p['date']}</p>
                  <p>{p['excerpt']}</p>
                </div>
              </a>
            </article>
            """
        )

    cards = "\n".join(cards_html) if cards_html else "<p>Žiadne články zatiaľ nie sú k dispozícii.</p>"

    html = f"""<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Faceless AI Blog</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Faceless AI Blog</h1>
    <div class="posts-grid">
      {cards}
    </div>
  </div>
</body>
</html>
"""
    return html


def update_index():
    ensure_dirs_and_placeholder()
    posts = load_posts()
    html = build_index_html(posts)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Index aktualizovaný: {INDEX_FILE} (počet článkov: {len(posts)})")


if __name__ == "__main__":
    update_index()
