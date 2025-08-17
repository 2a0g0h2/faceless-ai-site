import os

POSTS_DIR = "../posts"
OUTPUT_FILE = "../index.html"

def main():
    posts = []
    for f in os.listdir(POSTS_DIR):
        if f.endswith(".html"):
            posts.append({
                "filename": f,
                "title": f.replace("_", " ").replace(".html", ""),
                "date": os.path.getmtime(os.path.join(POSTS_DIR, f)),
                "cover_image": "images/default.jpg"  # optional: parse image from file if needed
            })

    posts.sort(key=lambda x: x["date"], reverse=True)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Main Page</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="main-container">
<h1>Latest Posts</h1>
<div class="posts-grid">
"""

    for post in posts:
        html += f"""
<div class="post-card">
    <a href="posts/{post['filename']}">
        <img src="{post['cover_image']}" alt="{post['title']}" class="card-image">
        <h2>{post['title']}</h2>
    </a>
</div>
"""

    html += """
</div>
</div>
</body>
</html>
"""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("Index updated!")

if __name__ == "__main__":
    main()

