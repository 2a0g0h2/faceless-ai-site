import os
import random
import datetime
import json

# Náhodné témy
TOPICS = [
    "The Future of Artificial Intelligence",
    "AI in Healthcare",
    "AI and Creativity",
    "The Rise of Generative Models",
    "Ethics of AI",
    "AI in Education",
    "AI and Climate Change",
    "The Future of Work with AI",
    "AI in Gaming",
    "AI and Human Emotions",
]

INTRO_TEMPLATES = [
    "Artificial Intelligence is rapidly transforming our world. In this article, we explore {topic} and what it means for the future.",
    "The topic of {topic} has become increasingly relevant in recent years. Let's dive deeper into how it affects us today.",
    "From research labs to our daily lives, {topic} is shaping the way we think about technology.",
]

CONCLUSION_TEMPLATES = [
    "In conclusion, {topic} will continue to be a driving force in shaping our future.",
    "As we've seen, {topic} is more than just a trend — it's a transformation.",
    "Ultimately, {topic} challenges us to think bigger and act smarter.",
]

def generate_article():
    topic = random.choice(TOPICS)
    intro = random.choice(INTRO_TEMPLATES).format(topic=topic)
    conclusion = random.choice(CONCLUSION_TEMPLATES).format(topic=topic)

    body = (
        f"<h2>Introduction</h2><p>{intro}</p>"
        f"<h2>Main Insights</h2><p>{topic} is impacting industries, research, and daily life. "
        f"We see innovations, but also challenges — ethical, social, and economic.</p>"
        f"<p>Experts suggest that while the potential is enormous, regulation, education, and awareness will be key "
        f"to ensuring positive outcomes.</p>"
        f"<h2>Conclusion</h2><p>{conclusion}</p>"
    )

    return topic, intro, body

def generate_cover_image(topic):
    # Jednoduchá reprezentácia obrázka
    return f"https://source.unsplash.com/1200x600/?technology,{topic.replace(' ', '')}"

def main():
    today = datetime.date.today().isoformat()
    topic, intro, body = generate_article()
    cover_image = generate_cover_image(topic)

    # HTML obsah
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{topic}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <div class="post-container">
    <div class="post-card">
      <img src="{cover_image}" alt="Cover image for {topic}" class="post-cover">
      <div class="post-content">
        <h1>{topic}</h1>
        {body}
      </div>
    </div>
  </div>
</body>
</html>"""

    # Uloženie
    os.makedirs("posts", exist_ok=True)
    base_path = f"posts/{today}-{topic.lower().replace(' ', '-')}"
    with open(base_path + ".html", "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(base_path + ".md", "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n{intro}\n\n{body}\n\n{cover_image}")
    with open(base_path + ".json", "w", encoding="utf-8") as f:
        json.dump({"title": topic, "intro": intro, "image": cover_image}, f)

if __name__ == "__main__":
    main()
