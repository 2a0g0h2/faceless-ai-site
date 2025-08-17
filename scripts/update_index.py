import os
import json
from datetime import datetime

POSTS_DIR = "../posts"
OUTPUT_FILE = "../index.html"

def load_posts():
    posts = []
    for file in os.listdir(POSTS_DIR):
        if file.endswith(".json"):
            path = os.path.join(POSTS_DIR, file)
            try:
                with open(path, "r") as f:
                    post = json.load(f)
                    # bezpečné získanie kľúčov
                    title = post.get("title", "Untitled")
                    date = post.get("date", "1970-01-01 00:00:00")
                    excerpt = post.get("excerpt", "")
                    cover_image = post.get("cover_image", "default.jpg")
                    posts.append({
                        "title": title,
                        "date": date,
                        "excerpt": excerpt,
                        "cover_image": cover_image,
                        "file_html": file.replace(".json", ".html")
                    })
            except Exception as e:
                print(f"Error loading {file}: {e}")
    return posts

def generate_index(posts):
    # zoradenie podľa dátumu zostupne
    posts.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d %H:%M:%S"), reverse=True)
    
    posts_html = ""
    for post in posts:
        posts_html += f"""
        <div class="post-preview">
            <a href="posts/{post['file_html']}">
                <h2>{post['title']}</h2>
                <img src="images/{post['cover_image']}" alt="{post['title']}" style="max-width:300px; height:auto;">
            </a>
            <p>{post['excerpt']}</p>
            <small>{post['date']}</small>
        </div>
        <hr>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Latest Articles</h1>
    {posts_html}
</body>
</html>
"""
    with open(OUTPUT_FILE, "w") as f:
        f.write(html_content)
    print(f"Index updated successfully with {len(posts)} posts!")

def main():
    posts = load_posts()
    if not posts:
        print("No posts found.")
        return
    generate_index(posts)

if __name__ == "__main__":
    main()
