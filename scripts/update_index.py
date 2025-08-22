import os
import json

def update_index():
    posts_dir = "posts"
    docs_dir = "docs"
    os.makedirs(docs_dir, exist_ok=True)

    posts = []
    for file in sorted(os.listdir(posts_dir), reverse=True):
        if file.endswith(".json"):
            with open(os.path.join(posts_dir, file), "r", encoding="utf-8") as f:
                post = json.load(f)
                slug = file.replace(".json", ".html")
                posts.append({
                    "title": post["title"],
                    "date": post["date"],
                    "image": post["image"],
                    "link": slug
                })

    content = "<html><body><h1>Latest Articles</h1><ul>"
    for post in posts:
        content += f"""
        <li>
            <h2><a href="{post['link']}">{post['title']}</a></h2>
            <img src="{post['image']}" alt="{post['title']}" style="max-width:600px;">
            <p><em>{post['date']}</em></p>
        </li>
        """
    content += "</ul></body></html>"

    with open(os.path.join(docs_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)

    print("Updated docs/index.html")

if __name__ == "__main__":
    update_index()
