import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "..", "posts")
INDEX_HTML = os.path.join(BASE_DIR, "..", "index.html")

def load_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):
            path = os.path.join(POSTS_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    post = json.load(f)
                    # Nastavenie defaultných hodnôt, ak niečo chýba
                    post.setdefault("title", "Untitled")
                    post.setdefault("date", "1970-01-01T00:00:00")
                    post.setdefault("excerpt", "")
                    post.setdefault("cover_image", "")
                    posts.append(post)
                except json.JSONDecodeError:
                    print(f"Chyba pri načítaní {filename}, preskočené.")
    # Zoradiť podľa dátumu, od najnovšieho
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts

def generate_index(posts):
    posts_html = ""
    for post in posts:
        posts_html += f"""
        <div class="post">
            <a href="posts/{post['title'].replace(' ', '_').replace(':','')}.html">
                <img src="{post['cover_image']}" alt="{post['title']}" style="max-width:200px;height:auto;">
                <h2>{post['title']}</h2>
                <p>{post['excerpt']}</p>
            </a>
        </div>
        """
    html = f"""
    <html>
    <head>
        <title>Faceless AI Site</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .post {{ margin-bottom: 30px; transition: transform 0.2s; }}
            .post:hover {{ transform: translateY(-5px); }}
            img {{ display:block; margin-bottom: 10px; }}
        </style>
    </head>
    <body>
        <h1>Faceless AI Blog</h1>
        {posts_html}
    </body>
    </html>
    """
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Index generated with {len(posts)} posts.")

def main():
    posts = load_posts()
    generate_index(posts)

if __name__ == "__main__":
    main()
