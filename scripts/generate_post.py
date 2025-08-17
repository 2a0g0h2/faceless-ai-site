import os
import random
import datetime

POSTS_DIR = "../posts"
IMAGES_SOURCE = "https://source.unsplash.com/800x400/?"

TOPICS = [
    "artificial intelligence", "technology", "business", "innovation",
    "cybersecurity", "future", "creativity", "science", "startups", "data"
]

def generate_excerpt(content, length=200):
    """Take the first sentence(s) as excerpt"""
    clean = content.replace("\n", " ")
    return clean[:length].rsplit(" ", 1)[0] + "..."

def generate_post():
    # pick topic
    topic = random.choice(TOPICS)
    title = f"{topic.title()} Insights {random.randint(100,999)}"
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"{date}-{title.replace(' ', '-')}.html"

    # generate fake article text (placeholder paragraphs)
    paragraphs = []
    for i in range(8):  # 8 odsekov
        p = f"This is paragraph {i+1} about {topic}. " + \
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 3
        paragraphs.append(p)

    content = "\n\n".join(f"<p>{p}</p>" for p in paragraphs)

    # excerpt
    excerpt = generate_excerpt(paragraphs[0])

    # cover image
    cover_image = f"{IMAGES_SOURCE}{topic.replace(' ', '%20')}"

    # HTML template
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <article class="post">
    <h1>{title}</h1>
    <p class="date">{date}</p>
    <img src="{cover_image}" alt="{topic}" class="cover">
    {content}
  </article>
</body>
</html>"""

    os.makedirs(POSTS_DIR, exist_ok=True)
    path = os.path.join(POSTS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    return {"filename": filename, "title": title, "date": date, "excerpt": excerpt, "cover": cover_image}

def main():
    post_data = generate_post()
    print("Generated:", post_data["filename"])

if __name__ == "__main__":
    main()
