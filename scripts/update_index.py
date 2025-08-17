import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "..", "posts")
INDEX_FILE = os.path.join(BASE_DIR, "..", "index.html")

def load_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):
            path = os.path.join(POSTS_DIR, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    post = json.load(f)
                    posts.append(post)
            except json.JSONDecodeError:
                print(f"Error reading {filename}")
    return posts

def generate_index(posts):
    posts_html = ""
    for post in posts:
        title = post.get("title", "Untitled")
        excerpt = post.get("excerpt", "")
        cover_image = post.get("cover_image", "")
        filename = f"{title.replace(' ', '_').replace(':','')}.html"
        posts_html += f"""
        <div class="post" style="margin-bottom:20px;">
            <a href="posts_html/{filename}" style="text-decoration:none;color:black;">
                <img src="{cover_image}" alt="{title}" style="max-width:300px;height:auto;display:block;margin-bottom:10px;">
                <h2>{title}</h2>
                <p>{excerpt}</p>
            </a>
        </div>
        """
    html = f"""
    <html>
    <head>
        <title>Faceless AI Site</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            .post img {{ transition: transform 0.3s; }}
            .post img:hover {{ transform: scale(1.05); }}
        </style>
    </head>
    <body>
        <h1>Latest Posts</h1>
        {posts_html}
    </body>
    </html>
    """
    return html

def main():
    posts = load_posts()
    posts.sort(key=lambda x: x.get("date","1970-01-01"), reverse=True)
    index_html = generate_index(posts)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"Index updated with {len(posts)} posts.")

if __name__ == "__main__":
    main()
