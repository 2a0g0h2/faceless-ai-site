import os
import json

POSTS_DIR = "posts"
INDEX_FILE = "index.html"

def update_index():
    posts = []
    for f in os.listdir(POSTS_DIR):
        if f.endswith(".json"):
            with open(os.path.join(POSTS_DIR, f), "r", encoding="utf-8") as jf:
                try:
                    data = json.load(jf)
                    posts.append(data)
                except Exception as e:
                    print(f"❌ Error reading {f}: {e}")

    # zoradíme podľa dátumu (najnovší hore)
    posts.sort(key=lambda x: x.get("date", ""), reverse=True)

    # vygenerujeme .html články
    for post in posts:
        slug = post["title"].replace(" ", "-").lower()
        html_file = os.path.join(POSTS_DIR, f"{slug}.html")

        html_content = f"""
        <html>
        <head>
            <title>{post['title']}</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>{post['title']}</h1>
            <img src="{post['image']}" alt="{post['title']}" style="max-width:600px;"><br>
            <p><i>{post['date']}</i></p>
            <p>{post['content']}</p>
            <p><a href="../index.html">← Back to Home</a></p>
        </body>
        </html>
        """

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content.strip())

    # vytvoríme index.html s kartami článkov
    cards = ""
    for post in posts:
        slug = post["title"].replace(" ", "-").lower()
        html_file = f"{POSTS_DIR}/{slug}.html"

        cards += f"""
        <div class="card">
            <a href="{html_file}">
                <img src="{post['image']}" alt="{post['title']}" onerror="this.src='images/default.png'">
                <h2>{post['title']}</h2>
                <p>{post['date']}</p>
            </a>
        </div>
        """

    html_template = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Faceless AI Blog</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background: #f9f9f9;
            }}
            .card {{
                display:inline-block;
                margin:15px;
                border:1px solid #ddd;
                padding:10px;
                width:220px;
                vertical-align:top;
                background:#fff;
                box-shadow:0 2px 5px rgba(0,0,0,0.1);
                border-radius:8px;
            }}
            img {{
                width:200px;
                height:150px;
                object-fit:cover;
                border-radius:4px;
            }}
            h1 {{ margin-bottom: 30px; }}
            h2 {{ font-size:18px; margin:10px 0; }}
            p {{ font-size:14px; color:#666; }}
        </style>
    </head>
    <body>
        <h1>Faceless AI Blog</h1>
        {cards}
    </body>
    </html>
    """

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_template.strip())

    print("✅ Index a články boli úspešne aktualizované.")

if __name__ == "__main__":
    update_index()
