import os
import json
from datetime import date
from openai import OpenAI

POSTS_DIR = "posts"
INDEX_FILE = "index.html"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- 1. Generate new post ---
def generate_post():
    topics = [
        "Top productivity hacks for remote workers",
        "AI tools revolutionizing small businesses",
        "Healthy lifestyle tips for busy professionals",
        "Latest trends in renewable energy",
        "How to start investing with little money",
        "Travel hacks for budget-friendly trips",
        "The future of electric vehicles",
        "Simple habits to improve mental health",
        "Top coding languages to learn in 2025",
        "How to build a successful side hustle"
    ]

    topic = topics[date.today().day % len(topics)]  # rotácia tém podľa dňa
    prompt = f"Write a blog post about: {topic}. The text should be informative, engaging, and at least 500 words."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content.strip()
    today = str(date.today())
    slug = topic.lower().replace(" ", "-")
    filename = f"{POSTS_DIR}/{today}-{slug}.json"

    post_data = {"title": topic, "date": today, "content": content}

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Generated new post: {filename}")
    return post_data

# --- 2. Update index.html ---
def update_index():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(POSTS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                posts.append(json.load(f))

    posts.sort(key=lambda x: x["date"], reverse=True)

    items = "\n".join(
        [f"<li><a href='posts/{p['date']}-{p['title'].lower().replace(' ', '-')}.html'>{p['title']}</a> - {p['date']}</li>" for p in posts]
    )

    html_content = f"""
    <html>
    <head>
        <title>Faceless AI Blog</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Faceless AI Blog</h1>
        <ul>
            {items}
        </ul>
    </body>
    </html>
    """

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_content.strip())

    print(f"✅ Updated {INDEX_FILE} with {len(posts)} posts")

# --- 3. Generate HTML pages for posts ---
def generate_pages():
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(POSTS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                post = json.load(f)

            slug = post["title"].lower().replace(" ", "-")
            html_filename = f"{POSTS_DIR}/{post['date']}-{slug}.html"

            html_content = f"""
            <html>
            <head>
                <title>{post['title']}</title>
                <meta charset="utf-8">
            </head>
            <body>
                <h1>{post['title']}</h1>
                <p><em>{post['date']}</em></p>
                <div>{post['content']}</div>
                <p><a href="../index.html">← Back to home</a></p>
            </body>
            </html>
            """

            with open(html_filename, "w", encoding="utf-8") as f:
                f.write(html_content.strip())

            print(f"✅ Generated page: {html_filename}")

# --- MAIN ---
if __name__ == "__main__":
    generate_post()
    update_index()
    generate_pages()
