import os, random, datetime

topics = [
    "AI in Healthcare", "Future of Work", "Climate Tech",
    "Space Exploration", "Neuroscience & AI", "Robotics in Daily Life",
    "Quantum Computing", "Virtual Reality Trends", "Ethics of AI"
]

def generate_article(topic):
    intro = f"<p><strong>{topic}</strong> is shaping our world in ways we couldn’t imagine just a decade ago. In this article, we’ll explore the latest insights.</p>"
    body = "".join([f"<p>{topic} insight {i+1}. This trend is influencing industries, technology, and our everyday lives.</p>" for i in range(random.randint(3,6))])
    conclusion = f"<p>In conclusion, {topic} is not just a buzzword – it’s a powerful movement changing the future. Stay tuned for more!</p>"
    return intro, body, conclusion

def save_post(title, intro, body, conclusion):
    date = datetime.date.today().isoformat()
    slug = title.lower().replace(" ", "-")
    filename = f"posts/{date}-{slug}"
    cover = "https://picsum.photos/1200/400"

    html = f"""<html><head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="../style.css">
    </head><body>
    <div class="post-container">
      <img src="{cover}" class="cover">
      <h1>{title}</h1>
      {intro}
      {body}
      {conclusion}
    </div>
    </body></html>"""

    md = f"""# {title}

![Cover Image]({cover})

{intro}

{body}

{conclusion}
"""

    with open(filename + ".html", "w", encoding="utf-8") as f:
        f.write(html)
    with open(filename + ".md", "w", encoding="utf-8") as f:
        f.write(md)

if __name__ == "__main__":
    os.makedirs("posts", exist_ok=True)
    topic = random.choice(topics)
    intro, body, conclusion = generate_article(topic)
    save_post(topic, intro, body, conclusion)
