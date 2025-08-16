import datetime
from pathlib import Path
from scripts.utils import get_trending_topic, get_unsplash_image_url, slugify

POSTS_DIR = Path("posts")
POSTS_DIR.mkdir(exist_ok=True)

def generate_article_text(topic):
    return f"""
# {topic}

In today's world, **{topic}** is becoming increasingly relevant. This article explores the importance of this trend, its implications, and what it means for the future.

## Why it matters
{topic} is shaping industries and societies at large. Staying informed can provide both opportunities and challenges.

## Looking ahead
As we continue to innovate and adapt, {topic} will likely influence our daily lives in profound ways.
"""

def build_index():
    posts = sorted(POSTS_DIR.glob("*.md"), reverse=True)
    links = []
    for post in posts:
        slug = post.stem
        html_file = slug + ".html"
        links.append(f'<li><a href="posts/{html_file}">{slug}</a></li>')

    index_path = Path("index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_list = "<ul>\n" + "\n".join(links) + "\n</ul>"
    content = content.replace("<ul>\n    <!-- Posts will be listed here -->\n  </ul>", new_list)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    topic = get_trending_topic()
    today = datetime.date.today().strftime("%Y-%m-%d")
    slug = slugify(topic)[:60]
    filename = f"{today}-{slug}.md"

    image_url = get_unsplash_image_url(topic)

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

    # Export HTML view
    html_name = filename.replace(".md", ".html")
    html_content = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{topic}</title>
<style>body{{font-family:system-ui,Segoe UI,Roboto,Arial,sans-serif;margin:20px;line-height:1.6;max-width:860px}}img{{max-width:100%;border-radius:12px}}h1{{margin-bottom:8px}}</style>
</head><body>
<a href="../index.html" style="text-decoration:none;">← Back</a>
<h1>{topic}</h1>
{f'<img src="{image_url}" alt="{topic}">' if image_url else ''}
<p><em>{today}</em></p>
<hr>
<div>{body.replace('\n','<br>')}</div>
</body></html>"""

    with open(POSTS_DIR / html_name, "w", encoding="utf-8") as fh:
        fh.write(html_content)

    build_index()
    print(f"Created: {POSTS_DIR / filename}")

if __name__ == "__main__":
    main()
