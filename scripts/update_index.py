import os
from pathlib import Path

POSTS_DIR = "posts"
INDEX_FILE = "index.html"

def update_index():
    posts = sorted(Path(POSTS_DIR).glob("*.html"), reverse=True)
    
    index_content = """
    <html>
        <head><title>AI Blog Index</title></head>
        <body>
            <h1>Latest Posts</h1>
            <ul>
    """

    for post in posts:
        post_name = post.stem
        img_path = f"images/{post_name}.png"
        index_content += f"""
            <li>
                <a href="{POSTS_DIR}/{post.name}">
                    <img src="{img_path}" alt="{post_name}" width="200"><br>
                    {post_name}
                </a>
            </li>
        """

    index_content += """
            </ul>
        </body>
    </html>
    """

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_content)

    print("Index updated successfully.")

if __name__ == "__main__":
    update_index()
