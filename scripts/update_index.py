import os

POSTS_DIR = "../posts"
INDEX_FILE = "../index.html"

def update_index():
    posts = []
    for f in sorted(os.listdir(POSTS_DIR), reverse=True):
        if f.endswith(".html"):
            with open(os.path.join(POSTS_DIR, f), "r", encoding="utf-8") as file:
                html = file.read()
                # Nájde nadpis článku
                try:
                    title = html.split("<h1>")[1].split("</h1>")[0]
                except IndexError:
                    title = "Neznámy článok"
                # Nájde obrázok
                try:
                    img = html.split('<img src="')[1].split('"')[0]
                except IndexError:
                    img = "../images/placeholder.png"
                posts.append({"title": title, "file": f, "img": img})
    
    index_html = """
    <html>
    <head>
        <link rel="stylesheet" href="style.css">
        <title>Faceless AI Site</title>
    </head>
    <body>
        <div class="container">
            <h1>Blog</h1>
            <div class="posts-grid">
    """
    for post in posts:
        index_html += f"""
        <div class="post-card">
            <a href="posts/{post['file']}">
                <img src="{post['img']}" alt="{post['title']}">
                <div class="post-card-content">
                    <h2>{post['title']}</h2>
                </div>
            </a>
        </div>
        """
    index_html += """
            </div>
        </div>
    </body>
    </html>
    """
    
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_html)
    
    print(f"Index aktualizovaný: {INDEX_FILE}")

if __name__ == "__main__":
    update_index()
