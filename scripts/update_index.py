import os
import datetime

POSTS_DIR = "posts"
INDEX_FILE = "../index.html"

def update_index():
    # zoznam článkov
    posts = []
    for f in os.listdir(POSTS_DIR):
        if f.endswith(".html"):
            path = os.path.join(POSTS_DIR, f)
            mtime = os.path.getmtime(path)
            posts.append((f, mtime))

    # zoradenie podľa dátumu
    posts.sort(key=lambda x: x[1], reverse=True)

    # vygenerovanie HTML
    post_items = ""
    for f, _ in posts:
        filepath = os.path.join(POSTS_DIR, f)
        with open(filepath, "r", encoding="utf-8") as pf:
            html = pf.read()

            # vyber title, excerpt a cover image
            title = html.split("<h1>")[1].split("</h1>")[0]
            date = html.split('<p class="date">')[1].split("</p>")[0]
            excerpt = html.split("<p>")[1].split("</p>")[0]
            cover = ""
            if '<img src="' in html:
                cover = html.split('<img src="')[1].split('"')[0]

        post_items += f"""
        <div class="post-card">
            <a href="posts/{f}">
                <img src="{cover}" alt="cover" class="thumb">
                <h2>{title}</h2>
                <p class="date">{date}</p>
                <p>{excerpt}</p>
            </a>
        </div>
        """

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Faceless AI Blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Faceless AI Blog</h1>
        <p>Daily auto-generated posts about AI, technology and the future 🚀</p>
    </header>
    <main class="post-grid">
        {post_items}
    </main>
</body>
</html>"""

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_html)

    print("✅ Index updated with", len(posts), "posts")

if __name__ == "__main__":
    update_index()
