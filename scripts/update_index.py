import os
import json

POSTS_DIR = "posts"
INDEX_FILE = "index.html"

def update_index():
    # načítaj všetky JSON články
    posts = [f for f in os.listdir(POSTS_DIR) if f.endswith(".json")]
    posts.sort(reverse=True)

    cards = ""
    for post in posts:
        path = os.path.join(POSTS_DIR, post)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        title = data.get("title", "Untitled")
        image = data.get("image", "static/images/default.png")
        slug = post.replace(".json", ".html")
        html_path = os.path.join(POSTS_DIR, slug)

        # ak HTML článok ešte neexistuje → vygeneruj ho
        if not os.path.exists(html_path):
            with open(html_path, "w", encoding="utf-8") as out:
                out.write(f"""
                <html>
                <head><title>{title}</title></head>
                <body>
                    <h1>{title}</h1>
                    <img src="{image}" alt="{title}" style="max-width:600px;">
                    <p>{data.get("content", "")}</p>
                </body>
                </html>
                """)

        # karta pre homepage
        cards += f"""
        <div class="card">
            <a href="{POSTS_DIR}/{slug}">
                <img src="{image}" alt="{title}" onerror="this.src='static/images/default.png'">
                <h2>{title}</h2>
            </a>
        </div>
        """

    html_template = f"""
    <html>
    <head>
        <title>Faceless AI Blog</title>
        <style>
            .card {{ display:inline-block; margin:10px; border:1px solid #ccc; padding:10px; width:220px; }}
            img {{ width:200px; height:150px; object-fit:cover; }}
        </style>
    </head>
    <body>
        <h1>Faceless AI Blog</h1>
        {cards}
    </body>
    </html>
    """

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    update_index()
