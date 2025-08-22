import os
import json

def generate_pages():
    os.makedirs("posts", exist_ok=True)
    for file in os.listdir("posts"):
        if not file.endswith(".json"):
            continue

        with open(os.path.join("posts", file), "r") as f:
            post = json.load(f)

        slug = file.replace(".json", ".html")
        with open(os.path.join("posts", slug), "w") as f:
            f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{post['title']}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <a href="../index.html">← Back</a>
    <h1>{post['title']}</h1>
    <p><em>{post['date']}</em></p>
    <img src="../{post['image']}" alt="{post['title']}" style="max-width:600px;"><br>
    <div class="content">
        {"<br><br>".join(post['content'].splitlines())}
    </div>
</body>
</html>""")

if __name__ == "__main__":
    generate_pages()
