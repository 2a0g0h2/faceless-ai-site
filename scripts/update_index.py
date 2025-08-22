import os
import json

def update_index():
    posts = []
    for file in os.listdir("posts"):
        if file.endswith(".json"):
            with open(os.path.join("posts", file), "r") as f:
                posts.append(json.load(f))

    posts.sort(key=lambda x: x["date"], reverse=True)

    with open("index.html", "w") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Faceless AI Blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Faceless AI Blog</h1>
    <div class="posts">
""")
        for post in posts:
            slug = f"posts/{post['date']}-{post['topic'].replace(' ', '_')}.html"
            f.write(f"""
    <div class="post">
        <h2><a href="{slug}">{post['title']}</a></h2>
        <p><em>{post['date']}</em></p>
        <img src="{post['image']}" alt="{post['title']}" style="max-width:300px;"><br>
    </div>
""")
        f.write("""
    </div>
</body>
</html>""")

if __name__ == "__main__":
    update_index()


if __name__ == "__main__":
    update_index()
