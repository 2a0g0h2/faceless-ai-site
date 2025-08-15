import os
import re
import random
import datetime
import requests
from pathlib import Path

# === CONFIG ===
OWNER = "2a0g0h2"
REPO  = "faceless-ai-site"
UNSPLASH_ACCESS_KEY = "6WT8TnP8wBB3rBA43R3WHkb3P_awqh4tp0prBsG6AnY"  # provided by user
POSTS_DIR = Path("content/posts")
IMAGES_DIR = Path("images")
INDEX_FILE = Path("index.html")

# Topics fallback (if Google Trends fetch fails)
FALLBACK_TOPICS = [
    "AI breakthroughs", "Crypto market", "Fitness habits", "Travel hacks",
    "Tech gadgets", "Space exploration", "Climate tech", "Startups",
    "Cybersecurity", "Gaming trends", "Electric vehicles", "Health science"
]

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text or "post"

def get_trending_topic() -> str:
    """Try Google Trends via pytrends. If unavailable, fall back to list."""
    try:
        from pytrends.request import TrendReq
        pytrends = TrendReq(hl='en-US', tz=0)
        df = pytrends.trending_searches(pn='united_states')
        topic = df.iloc[0, 0]
        return str(topic)
    except Exception:
        return random.choice(FALLBACK_TOPICS)

def get_unsplash_image_url(query: str) -> str:
    url = f"https://api.unsplash.com/photos/random?query={requests.utils.quote(query)}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    data = r.json()
    return data["urls"]["regular"]

def generate_article_text(topic: str) -> str:
    today = datetime.date.today().strftime("%B %d, %Y")
    intro_styles = [
        f"Here's a quick, no-fluff look at {topic} — what's happening right now and why it matters.",
        f"{topic} keeps making headlines. Below is a short, practical rundown you can skim in under 3 minutes.",
        f"If you've seen {topic} everywhere today, you're not alone. Here's what to know, fast."
    ]
    intro = random.choice(intro_styles)

    bullets = [
        f"**What it is:** A snapshot of {topic} as of {today}.",
        "**Why people care:** Signal vs. noise — the bits that might actually matter.",
        "**What to watch:** A few realistic near‑term developments.",
    ]

    mids = [
        "## Key points\n" + "\n".join([f"- {b}" for b in bullets]),
        "## Quick context\n- This is changing quickly.\n- Expect updates and course-corrections.",
        "## The signal\n- Separate hype from facts.\n- Track measurable milestones."
    ]
    mid = random.choice(mids)

    closing = random.choice([
        "If you're short on time, bookmark this — we refresh daily.",
        "We'll keep tracking this story. Come back tomorrow for a fresh roundup.",
        "No spammy takes — just the useful parts. See you tomorrow."
    ])

    return f"""{intro}

{mid}

### Bottom line
{closing}
"""

def build_index():
    items = []
    for p in sorted(POSTS_DIR.glob("*.md")):
        title = None
        date = None
        with open(p, "r", encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        if len(lines) >= 3 and lines[0].strip() == "---":
            for i in range(1, min(40, len(lines))):
                line = lines[i]
                if line.startswith("title:"):
                    title = line.split(":",1)[1].strip().strip('"')
                if line.startswith("date:"):
                    date = line.split(":",1)[1].strip().strip('"')
                if line.strip() == "---":
                    break
        if not title:
            title = p.stem
        items.append((p.name, title, date))

    items.sort(reverse=True)

    html_items = []
    for name, title, date in items[:200]:
        html_items.append(f'<li><a href="content/posts/{name}">{title}</a> <small>{date or ""}</small></li>')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Faceless AI Site</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 0; background:#0b0c10; color:#eaeef3; }}
    header {{ padding: 32px 20px; text-align:center; background:#111318; position:sticky; top:0; }}
    h1 {{ margin:0; font-size: 28px; }}
    main {{ max-width: 900px; margin: 24px auto; padding: 0 16px; }}
    .card {{ background:#151821; padding:20px; border-radius:16px; box-shadow:0 10px 30px rgba(0,0,0,.25); }}
    ul.posts {{ list-style:none; padding:0; margin:0; display:grid; gap:12px; }}
    ul.posts li a {{ color:#91c6ff; text-decoration:none; }}
    ul.posts li a:hover {{ text-decoration:underline; }}
    footer {{ text-align:center; color:#9aa4b2; padding:30px; }}
  </style>
</head>
<body>
  <header>
    <h1>Faceless AI — Daily Trends</h1>
    <p style="margin:8px 0 0; color:#9aa4b2;">Auto‑published once per day. No fluff.</p>
  </header>
  <main>
    <div class="card">
      <h2 style="margin-top:0;">Latest posts</h2>
      <ul class="posts">
        {''.join(html_items) or '<li>No posts yet. First one arrives after the action runs.</li>'}
      </ul>
    </div>
  </main>
  <footer>© {datetime.date.today().year} Faceless AI</footer>
</body>
</html>"""
    INDEX_FILE.write_text(html, encoding="utf-8")

def main():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

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

    # Also export quick HTML view for the post
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
<div>{body.replace('\n','<br>')}</div>
</body></html>"""
    with open(POSTS_DIR / html_name, "w", encoding="utf-8") as fh:
        fh.write(html_content)

    build_index()
    print(f"Created: {POSTS_DIR / filename}")

if __name__ == "__main__":
    main()
