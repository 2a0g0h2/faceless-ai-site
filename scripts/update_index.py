import os
import datetime

POSTS_DIR = "../posts"
INDEX_FILE = "../index.html"

def get_posts():
    posts = []
    for file in os.listdir(POSTS_DIR):
        if file.endswith(".html"):
            path = os.path.join(POSTS_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract title
            title_start = content.find("<h1>") + 4
            title_end = content.find("</h1>")
            title = content[title_start:title_end].strip()

            # Extract date
            date_start = content.find('<p class="date">') + len('<p class="date">')
            date_end = content.find("</p>", date_start)
            date = content[date_start:date_end].strip()

            # Extract excerpt = first <p> after date
            first_p_start = content.find("<p>", date_end) + 3
            first_p_end = content.find("</p>", first_p_start)
            excerpt = content[first_p_start:first_p_end].strip()

            # Extract cover
            img_start = content.find('<img src="') + len('<img src="')
            img_end = content.find('"', img_start)
            cover = content[img_start:img_end]

            posts.append({
                "file": file,
                "title": title,
                "date": date,
                "excerpt": excerpt,
                "cover": cover
            })

    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts

def build_index(posts):
    cards = ""
    for post in posts:
        cards += f"""
        <div class="card">
          <a href="posts/{post['file']}">
            <img src="{post['cover']}" alt="{post['title']}">
            <h2>{post['title']}</h2>
          </a>
          <p class="date">{post['date']}</p>
          <p>{post['excerpt']}</p>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Faceless AI Blog</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Faceless AI Blog</h1>
  <div class="grid">
    {cards}
  </div>
</body>
</html>"""
    return html

def main():
    posts = get_posts()
    html = build_index(posts)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html updated with", len(posts), "posts")

if __name__ == "__main__":
    main()
