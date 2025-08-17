import os

POSTS_DIR = "posts"
INDEX_FILE = "index.html"

def update_index():
    posts = []

    for f in os.listdir(POSTS_DIR):
        if f.endswith(".html"):
            path = os.path.join(POSTS_DIR, f)
            with open(path, "r", encoding="utf-8") as file:
                html = file.read()

                # titulok
                if "<h1>" in html:
                    title = html.split("<h1>")[1].split("</h1>")[0]
                else:
                    title = f

                # dátum
                if '<p class="date">' in html:
                    date = html.split('<p class="date">')[1].split("</p>")[0]
                else:
                    date = "Unknown date"

                # obrázok
                if '<img src="' in html:
                    image = html.split('<img src="')[1].split('"')[0]
                else:
                    image = "https://source.unsplash.com/800x400/?abstract,ai"

                posts.append((date, title, f, image))

    # zoradíme podľa dátumu (najnovšie hore)
    posts.sort(reverse=True, key=lambda x: x[0])

    cards = ""
    for date, title, filename, image in posts:
        cards += f"""
        <div class="post-card">
            <a href="posts/{filename}">
                <img src="{image}" alt="{title}">
                <h2>{title}</h2>
                <p class="date">{date}</p>
            </a>
        </div>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Faceless AI Blog</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="container">
            <h1>Faceless AI Blog</h1>
            <div class="posts-grid">
                {cards}
            </div>
        </div>
    </body>
    </html>
    """

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ index.html updated!")

if __name__ == "__main__":
    update_index()
