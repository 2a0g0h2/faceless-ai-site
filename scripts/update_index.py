import os, glob

posts = []
for file in sorted(glob.glob("posts/*.html"), reverse=True):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    title_start = content.find("<h1>")
    title_end = content.find("</h1>")
    title = content[title_start+4:title_end] if title_start != -1 else "Untitled"
    posts.append((os.path.basename(file), title))

cards = ""
for filename, title in posts:
    cards += f"""
    <div class="card">
        <img src="https://picsum.photos/400/200" alt="Cover">
        <h2>{title}</h2>
        <a href="posts/{filename}" class="btn">Read more</a>
    </div>
    """

index_html = f"""<html><head>
<meta charset="UTF-8">
<title>Faceless AI Blog</title>
<link rel="stylesheet" href="style.css">
</head><body>
<h1>Faceless AI Blog</h1>
<div class="grid">
{cards}
</div>
</body></html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
