import os
import json

def main():
    posts = []
    for file in os.listdir("posts"):
        if file.endswith(".json"):
            with open(os.path.join("posts", file)) as f:
                posts.append(json.load(f))

    posts.sort(key=lambda x: x["date"], reverse=True)

    cards_html = ""
    for post in posts:
        slug = f"{post['date']}-{post['title'].lower().replace(' ', '-')}.html"
        cards_html += f"""
        <div class="card">
            <img src="{post['image']}" alt="{post['title']}">
            <h2>{post['title']}</h2>
            <p>{post['excerpt']}</p>
            <a href="posts/{slug}" class="btn">Read More</a>
        </div>
        """

    html = f"""
<html>
  <head>
    <title>AI Blog</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>AI Daily Insights</h1>
    <div class="grid">
      {cards_html}
    </div>
  </body>
</html>
    """

    with open("index.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    main()
