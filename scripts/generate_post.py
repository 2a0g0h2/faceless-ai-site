import os
import random
import json
from datetime import datetime

# --- Nastavenie cesty k priečinku images ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # cesta ku scripts/
IMAGES_DIR = os.path.join(BASE_DIR, "..", "images")    # ../images vzhľadom na scripts/
POSTS_DIR = os.path.join(BASE_DIR, "..", "posts")

# --- Funkcia na výber náhodného obrázku ---
def get_random_image():
    imgs = [f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    if not imgs:
        return None
    return os.path.join("../images", random.choice(imgs))

# --- Funkcia na generovanie článku ---
def generate_article():
    title = "Test Article " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = datetime.now().isoformat()
    excerpt = "This is a short excerpt for the article."
    body = """
    <h2>Introduction</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    <h2>Main Content</h2>
    <p>Vestibulum nec odio ipsum. Suspendisse cursus malesuada facilisis.</p>
    <h2>Conclusion</h2>
    <p>Donec vel mauris quam. Integer mollis nulla at sapien.</p>
    """
    cover_image = get_random_image() or ""

    return {
        "title": title,
        "date": date_str,
        "excerpt": excerpt,
        "body": body,
        "cover_image": cover_image
    }

# --- Uloženie článku ---
def save_article(article):
    filename_base = article["title"].replace(" ", "_").replace(":", "")
    md_path = os.path.join(POSTS_DIR, filename_base + ".md")
    html_path = os.path.join(POSTS_DIR, filename_base + ".html")
    json_path = os.path.join(POSTS_DIR, filename_base + ".json")

    # Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {article['title']}\n\n{article['body']}")

    # HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"""
        <html>
        <head><title>{article['title']}</title></head>
        <body>
        <img src="{article['cover_image']}" style="max-width:100%;height:auto;">
        {article['body']}
        </body>
        </html>
        """)

    # JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(article, f, ensure_ascii=False, indent=4)

# --- Hlavná funkcia ---
def main():
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)
    article = generate_article()
    save_article(article)
    print(f"Article '{article['title']}' generated.")

if __name__ == "__main__":
    main()
