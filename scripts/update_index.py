import os
from datetime import datetime

POSTS_DIR = "../posts"
INDEX_FILE = "../index.html"

def update_index():
    posts = []
    os.makedirs(POSTS_DIR, exist_ok=True)

    for f in os.listdir(POSTS_DIR):
        if f.endswith(".html"):
            filepath = os.path.join(POSTS_DIR, f)
            with open(filepath, "r", encoding="utf-8") as file:
                html = file.read()
            
            # Extract title
            title = html.split("<title>")[1].split("</title>")[0] if "<title>" in html else f
            
            # Extract date
            date = html.split('<p class="date">')[1].split("</p>")[0] if '<p class="date">' in html else "Unknown Date"
            
            # Extract first image
            if "<img" in html:
                image = html.split("<img")[1].split(">")[0]
                image = "<img" + image + ">"
            else:
                image = '<img src="https://source.unsplash.com/400x200/?ai" alt="AI">'
            
            posts.append({
                "filename": f,
                "title": title,
                "date": date,
                "image": image
            })

    # Sort posts by date (descending)
    posts.sort(key=lambda x: x["filename"], reverse=True)

    # Build HTML
    cards = []
    for post in posts:
        card = f"""
        <div class="post-card">
            <a href="posts/{post['filename']}">
                <div class="thumbnail">{post['image']}</div>
                <h2>{post['title']}</h2>
                <p class="date">{post['date']}</p>
            </a>
        </div>
        """
        cards.append(card)

    content = "\n".join(cards)

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Faceless AI Blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Faceless AI Blog</h1>
        <p class="subtitle">Daily insights into AI, technology, and the future</p>
    </header>
    <main>
        <div class="post-grid">
            {content}
        </div>
    </main>
    <footer>
        <p>&copy; {datetime.now().year} Faceless AI</p>
    </footer>
</body>
</html>
"""

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_html)

    print("✅ index.html updated successfully!")

if __name__ == "__main__":
    update_index()

