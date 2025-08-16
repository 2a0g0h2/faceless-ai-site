import os
import random
import datetime
import requests
from pathlib import Path

POSTS_DIR = Path("posts")
POSTS_DIR.mkdir(exist_ok=True)

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "6WT8TnP8wBB3rBA43R3WHkb3P_awqh4tp0prBsG6An")

def get_unsplash_image_url(query: str) -> str:
    try:
        url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data["urls"]["regular"]
    except Exception as e:
        print(f"Unsplash error: {e}")
        return ""

def slugify(text: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in text.lower()).strip("-")

def get_trending_topic() -> str:
    topics = [
        "Artificial Intelligence",
        "Space Exploration",
        "Quantum Computing",
        "Sustainable Energy",
        "Climate Change",
        "Virtual Reality",
        "Blockchain Technology",
        "Cybersecurity",
        "Neuroscience",
        "Future of Work"
    ]
    return random.choice(topics)

def generate_article_text(topic: str) -> str:
    return (
        f"# {topic}\n\n"
        f"This article explores the fascinating topic of **{topic}**.\n\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Donec vel sapien eget nunc pretium tincidunt. "
        "Suspendisse potenti. In vitae facilisis nisl. "
        "Integer malesuada, neque ac ullamcorper placerat, "
        "justo metus vulputate metus, non facilisis elit nisl a sapien.\n\n"
        "## Key Insights\n\n"
        "- Point one about the topic.\n"
        "- Another important aspect.\n"
        "- Future perspectives and potential impacts.\n\n"
        "Stay tuned for more daily insights!"
    )

def build_index():
    files = sorted(POSTS_DIR.glob("*.md"), reverse=True)
    links = []
    for f in files:
        name = f.stem
        links.append(f'<li><a href="posts/{f.stem}.html">{name}</a></li>')

    index_content = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Daily AI Blog</title>
<style>body{{font-family:system-ui,Segoe UI,Roboto,Arial,sans-serif;margin:20px;line-height:1.6;max-width:860px}}a{{text-decoration:none;color:#0366d6}}</style>
</head><body>
<h1>Daily AI Blog</h1>
<ul>
{''.join(links)}
</ul>
</body></html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)

def main():
    topic = get_trending_topic()
    today = datetime.date.today().strftime("%Y-%m-%d")
    slug = slugify(topic)[:60]
    filename = f"{today}-{slug}.md"

    try:
        image_url = get_unsplash_image_url(topic)
    except Exception:
        image_url = ""

    body = generate_article_text(topic)
    front_matter = [
        "---",
        f'title: "{topic}"',
        f'date: "{today}"',
        f'image: "{image_url}"',
        f'slug: "{slug}"',
        "---",
        "",
    ]
    content = "\n".join(front_matter) + body + (f"\n\n![{topic}]({image_url})\n" if image_url else "\n")

    with open(POSTS_DIR / filename, "w", encoding="utf-8") as f:
        f.write(content)

    body_html = body.replace("\n", "<br>")
    html_name = filename.replace(".md", ".html")
    html_content = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{topic}</title>
<style>body{{font-family:system-ui,Segoe UI,Roboto,Arial,sans-serif;margin:20px;line-height:1.6;max-width:860px}}img{{max-width:100%;border-radius:12px}}h1{{margin-bottom:8px}}</style>
</head><body>
<a href="../../index.html" style="text-decoration:none;">← Back</a>
<h1>{topic}</h1>
{f'<img src="{image_url}" alt="{topic}">' if image_url else ''}
<p><em>{today}</em></p>
<hr>
<div>{body_html}</div>
</body></html>"""

    with open(POSTS_DIR / html_name, "w", encoding="utf-8") as fh:
        fh.write(html_content)

    build_index()
    print(f"Created: {POSTS_DIR / filename}")

if __name__ == "__main__":
    main()
