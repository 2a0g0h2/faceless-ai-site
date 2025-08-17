import os

POSTS_DIR = "posts"
IMAGES_DIR = "static/images"
INDEX_FILE = "index.html"

def update_index():
    posts = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
    posts.sort(reverse=True)  # Najnovšie hore

    cards = ""
    for post in posts:
        slug = post.replace(".html", "")
        img_path = f"images/{slug}.png"
        cards += f"""
        <div class="card">
            <a href="{POSTS_DIR}/{post}">
                <img src="{img_path}" alt="{slug}" onerror="this.src='images/default.png'">
                <h2>{slug.replace('-', ' ').title()}</h2>
            </a>
        </div>
        """

    html_template = f"""
    <html>
    <head>
        <title>Faceless AI Blog</title>
        <style>
            .card {{ display:inline-block; margin:10px; border:1px solid #ccc; padding:10px; }}
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
