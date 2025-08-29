import os
import json
import requests
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")

POSTS_DIR = "posts"
SITE_DIR = "site"

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(SITE_DIR, exist_ok=True)

# ====== FUNKCIA NA ZÍSKANIE OBRÁZKU ======
def fetch_image(query):
    if not PIXABAY_API_KEY:
        return None
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&image_type=photo&per_page=3"
    try:
        r = requests.get(url)
        data = r.json()
        if "hits" in data and len(data["hits"]) > 0:
            return data["hits"][0]["webformatURL"]
    except Exception as e:
        print("Image fetch error:", e)
    return None

# ====== GENEROVANIE ČLÁNKU ======
def generate_post():
    topic_prompt = "Generate a trending blog post topic in technology, science, lifestyle, or productivity."
    topic_resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": topic_prompt}],
    )
    topic = topic_resp.choices[0].message.content.strip()

    content_prompt = f"Write a detailed blog post (500-700 words) about: {topic}."
    content_resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content_prompt}],
    )
    content = content_resp.choices[0].message.content.strip()

    slug = topic.lower().replace(" ", "-").replace(".", "")
    date = datetime.now().strftime("%Y-%m-%d")

    image_url = fetch_image(topic) or "https://via.placeholder.com/800x400"

    post = {
        "title": topic,
        "date": date,
        "content": content,
        "image": image_url,
        "slug": slug
    }

    filename = os.path.join(POSTS_DIR, f"{date}-{slug}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=2)

    return post

# ====== GENEROVANIE INDEX.HTML ======
def generate_index(posts):
    html = """
    <html>
    <head>
        <meta charset='utf-8'>
        <title>Faceless AI Blog</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #121212; color: #eee; }
            .post { display: inline-block; width: 300px; margin: 15px; background: #1e1e1e; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.4); transition: transform 0.3s; }
            .post:hover { transform: scale(1.05); }
            .post img { width: 100%; height: 180px; object-fit: cover; }
            .post h2 { font-size: 18px; margin: 15px; color: #fff; }
            .post a { text-decoration: none; color: inherit; }
        </style>
    </head>
    <body>
        <h1>Faceless AI Blog</h1>
        <div style="display:flex; flex-wrap: wrap;">
    """

    for post in posts:
        html += f"""
        <div class="post">
            <a href="{post['slug']}.html">
                <img src="{post['image']}" alt="cover">
                <h2>{post['title']}</h2>
            </a>
        </div>
        """

    html += """
        </div>
    </body>
    </html>
    """

    with open(os.path.join(SITE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

# ====== GENEROVANIE STRÁNKY ČLÁNKU ======
def generate_post_page(post):
    html = f"""
    <html>
    <head>
        <meta charset='utf-8'>
        <title>{post['title']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #121212; color: #eee; }}
            h1 {{ color: #fff; }}
            img {{ max-width: 100%; border-radius: 12px; margin-bottom: 20px; }}
            a {{ color: #4da6ff; }}
        </style>
    </head>
    <body>
        <a href="index.html">← Back</a>
        <h1>{post['title']}</h1>
        <p><em>{post['date']}</em></p>
        <img src="{post['image']}" alt="cover">
        <p>{post['content'].replace('\n', '<br>')}</p>
    </body>
    </html>
    """

    with open(os.path.join(SITE_DIR, f"{post['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)

# ====== HLAVNÁ FUNKCIA ======
def main():
    post = generate_post()

    posts = []
    for filename in os.listdir(POSTS_DIR):
        with open(os.path.join(POSTS_DIR, filename), encoding="utf-8") as f:
            posts.append(json.load(f))

    posts = sorted(posts, key=lambda x: x["date"], reverse=True)

    generate_index(posts)
    for p in posts:
        generate_post_page(p)

if __name__ == "__main__":
    main()
