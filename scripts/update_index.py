# scripts/update_index.py
import os
import json

posts_dir = "posts"
index_file = "../index.html"

posts = []
for fname in os.listdir(posts_dir):
    if fname.endswith(".json"):
        with open(os.path.join(posts_dir, fname), "r", encoding="utf-8") as f:
            data = json.load(f)
            # kontrola, aby sme mali všetky polia
            posts.append({
                "title": data.get("title", "Untitled"),
                "excerpt": data.get("intro", "")[:150] + "...",
                "image": data.get("image", ""),
                "date": data.get("date", "1970-01-01"),
                "filename": fname.replace(".json", ".html")
            })

posts.sort(key=lambda x: x["date"], reverse=True)

cards_html = ""
for post in posts:
    cards_html += f"""
    <div class="post-card">
      <img src="{post['image']}" alt="{post['title']}">
      <h2>{post['title']}</h2>
      <p>{post['excerpt']}</p>
      <a href="posts/{post['filename']}">Read more</a>
    </div>
    """

with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

# nahradiť div s id=posts-grid
import re
index_content = re.sub(r'(<div id="posts-grid".*?>).*?(</div>)', r'\1' + cards_html + r'\2', index_content, flags=re.DOTALL)

with open(index_file, "w", encoding="utf-8") as f:
    f.write(index_content)
