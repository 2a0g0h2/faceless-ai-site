import os
import requests
from PIL import Image
import frontmatter
import markdown
from slugify import slugify

POSTS_DIR = "posts"
IMAGES_DIR = "static/images"

def generate_post():
    # Príklad dát (tu môže byť tvoj AI generátor)
    title = "Testovací článok"
    content = "Toto je obsah článku..."
    image_url = "https://via.placeholder.com/600x400"

    # Vytvor slug pre názov súboru
    slug = slugify(title)
    post_md_file = os.path.join(POSTS_DIR, f"{slug}.md")
    post_html_file = os.path.join(POSTS_DIR, f"{slug}.html")
    image_file = os.path.join(IMAGES_DIR, f"{slug}.png")

    # Stiahni obrázok
    img_data = requests.get(image_url).content
    os.makedirs(IMAGES_DIR, exist_ok=True)
    with open(image_file, "wb") as f:
        f.write(img_data)

    # Ulož markdown
    os.makedirs(POSTS_DIR, exist_ok=True)
    post = frontmatter.Post(content, title=title)
    with open(post_md_file, "w", encoding="utf-8") as f:
        frontmatter.dump(post, f)

    # Prevod do HTML
    html_content = markdown.markdown(content)
    html_template = f"""
    <html>
    <head><title>{title}</title></head>
    <body>
        <h1>{title}</h1>
        <img src="../{image_file}" alt="{title}">
        {html_content}
    </body>
    </html>
    """
    with open(post_html_file, "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    generate_post()
