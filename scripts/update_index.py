import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "..", "posts")
INDEX_FILE = os.path.join(BASE_DIR, "..", "index.html")
POSTS_HTML_DIR = os.path.join(BASE_DIR, "..", "posts_html")

os.makedirs(POSTS_HTML_DIR, exist_ok=True)

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
        <div class="post">
            <a href="posts_html/{filename}">
                <img src="{cover_image}" alt="{title}">
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
            body {{
                font-family: Arial, sans-serif;
                background-color: #1e1e1e;
                color: #f0f0f0;
                padding: 20px;
            }}
            a {{ color: inherit; text-decoration: none; }}
            .post {{
                margin-bottom: 30px;
                transition: transform 0.3s;
            }}
            .post:hover {{ transform: translateY(-5px); }}
            .post img {{
                max-width: 300px;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.5);
                display: block;
                margin-bottom: 10px;
            }}
            h1 {{ margin-bottom: 40px; }}
        </style>
    </head>
    <body>
        <h1>Latest Posts</h1>
        {posts_html}
    </body>
    </html>
    """
    return html

def generate_post_html(post):
    title = post.get("title", "Untitled")
    content = post.get("content", "")
    cover_image = post.get("cover_image", "")
    filename = f"{title.replace(' ', '_').replace(':','')}.html"
    filepath = os.path.join(POSTS_HTML_DIR, filename)

    html = f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #121212;
                color: #f0f0f0;
                padding: 40px;
                max-width: 800px;
                margin: auto;
            }}
            img {{
                max-width: 100%;
                height: auto;
                border-radius: 10px;
                margin-bottom: 20px;
            }}
            h1 {{ margin-bottom: 20px; }}
            p {{ line-height: 1.6; margin-bottom: 15px; }}
            a {{ color: #ffa500; }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <img src="{cover_image}" alt="{title}">
        {content}
        <p><a href="../index.html">← Back to Index</a></p>
    </body>
    </html>
    """

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    posts = load_posts()
    posts.sort(key=lambda x: x.get("date","1970-01-01"), reverse=True)
    
    for post in posts:
        generate_post_html(post)

    index_html = generate_index(posts)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_html)

    print(f"Index updated with {len(posts)} posts.")

if __name__ == "__main__":
    main()
