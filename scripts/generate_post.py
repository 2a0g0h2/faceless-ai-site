import os
import random
import datetime
import requests

# Cesty
POSTS_DIR = "posts"
TEMPLATE_FILE = "templates/post_template.html"
INDEX_FILE = "index.html"

# Unsplash API – náhodné obrázky
UNSPLASH_URL = "https://source.unsplash.com/800x600/?technology,ai,future,abstract"

def get_random_image():
    return UNSPLASH_URL

def generate_content():
    """Vygeneruje článok s odsekmi a podnadpismi."""
    paragraphs = [
        "Artificial Intelligence (AI) is rapidly transforming the way we interact with technology. From personalized recommendations to self-driving cars, the applications are vast and evolving every day.",
        "One of the most fascinating aspects of AI is its ability to learn and adapt. Unlike traditional software, machine learning models improve with more data, creating smarter systems over time.",
        "AI also raises important ethical questions. Issues such as bias in algorithms, privacy, and the future of work are central to the debate about how we should use these technologies.",
        "Despite the challenges, the future of AI looks promising. It has the potential to revolutionize industries, improve healthcare, and even assist in tackling climate change."
    ]

    # Podnadpisy
    headers = [
        "Introduction to AI",
        "The Power of Machine Learning",
        "Ethical Considerations",
        "The Road Ahead"
    ]

    # Kombinácia do HTML
    content = ""
    for h, p in zip(headers, paragraphs):
        content += f"<h2>{h}</h2>\n<p>{p}</p>\n"

    return content

def create_post():
    """Vytvorí nový článok podľa šablóny."""
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    title = f"Daily AI Insights - {date_str}"
    filename = f"{date_str}-post.html"
    filepath = os.path.join(POSTS_DIR, filename)

    # Načítať šablónu
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    # Vložiť obsah
    cover_image = get_random_image()
    content = generate_content()

    post_html = template.format(
        title=title,
        date=date_str,
        cover_image=cover_image,
        content=content
    )

    # Uložiť článok
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(post_html)

    return filename, title, cover_image

def update_index(posts_data):
    """Aktualizuje index.html so zoznamom článkov."""
    posts_html = ""
    for filename, title, cover in posts_data:
        posts_html += f"""
        <div class="post-card">
            <a href="posts/{filename}">
                <img src="{cover}" alt="{title}">
                <div class="post-card-content">
                    <h2>{title}</h2>
                    <p>Read more...</p>
                </div>
            </a>
        </div>
        """

    index_html = f"""
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
                {posts_html}
            </div>
        </div>
    </body>
    </html>
    """

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_html)

def main():
    os.makedirs(POSTS_DIR, exist_ok=True)

    # Vytvoriť nový post
    filename, title, cover = create_post()

    # Načítať existujúce
    posts = []
    for f in os.listdir(POSTS_DIR):
        if f.endswith(".html"):
            path = os.path.join(POSTS_DIR, f)
            date_str = f.split("-post.html")[0]
            posts.append((f, f"Daily AI Insights - {date_str}", cover))

    # Zoradiť podľa dátumu (najnovšie hore)
    posts.sort(reverse=True)

    # Aktualizovať index
    update_index(posts)

if __name__ == "__main__":
    main()
