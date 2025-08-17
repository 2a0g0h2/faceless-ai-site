import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "..", "posts")
POST_PAGES_DIR = os.path.join(BASE_DIR, "..", "posts_html")  # nový priečinok

os.makedirs(POST_PAGES_DIR, exist_ok=True)

def generate_post_html(post):
    title = post.get("title", "Untitled")
    date = post.get("date", "")
    excerpt = post.get("excerpt", "")
    cover_image = post.get("cover_image", "")

    html = f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            img {{ max-width: 100%; height: auto; }}
            h1 {{ margin-bottom: 5px; }}
            p {{ line-height: 1.6; }}
        </style>
    </head>
    <body>
        <a href="../index.html">← Back to home</a>
        <h1>{title}</h1>
        <p><em>{date}</em></p>
        <img src="{cover_image}" alt="{title}">
        <p>{excerpt}</p>
    </body>
    </html>
    """
    filename = f"{title.replace(' ', '_').replace(':','')}.html"
    filepath = os.path.join(POST_PAGES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {filename}")

def main():
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):
            path = os.path.join(POSTS_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    post = json.load(f)
                    generate_post_html(post)
                except json.JSONDecodeError:
                    print(f"Error reading {filename}")

if __name__ == "__main__":
    main()
