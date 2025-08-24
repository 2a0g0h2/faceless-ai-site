import os
import json
import random
import openai
from datetime import datetime

# API key
openai.api_key = os.getenv("OPENAI_API_KEY")

POSTS_DIR = "posts"
IMAGES_DIR = "static/images"

# topics pool
TOPICS = [
    "Future of Artificial Intelligence",
    "Impact of AI on Creativity",
    "Ethics of AI in Daily Life",
    "How AI is Changing Business",
    "AI and Human Emotions",
    "AI in Education",
    "AI and Cybersecurity",
    "AI in Healthcare",
    "AI and Climate Change",
    "AI in Entertainment"
]

def generate_article(topic):
    """Generate an article around 800 words with intro, body (paragraphs, subheadings), and conclusion."""
    prompt = f"""
    Write a well-structured article of about 800 words on the topic: "{topic}".
    - Start with an engaging introduction (2 paragraphs).
    - Add 2–3 subheadings with relevant sections (use ### Subheading style).
    - Write clear, flowing paragraphs (4–6 sentences each).
    - End with a short conclusion (2 paragraphs).
    - Do not use bullet points, only paragraphs and subheadings.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1600,
        temperature=0.7
    )

    text = response.choices[0].text.strip()
    return text

def format_to_html(text):
    """Convert raw text into HTML with <p> and <h2> tags."""
    paragraphs = text.split("\n")
    html_content = ""
    for i, p in enumerate(paragraphs):
        if len(p.strip()) > 0:
            if i == 0:
                html_content += f"<p><em>{p.strip()}</em></p>\n"   # intro
            elif "###" in p:  
                html_content += f"<h2>{p.replace('###','').strip()}</h2>\n"
            else:
                html_content += f"<p>{p.strip()}</p>\n"
    return html_content

def generate_post():
    topic = random.choice(TOPICS)
    raw_article = generate_article(topic)
    html_content = format_to_html(raw_article)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}.html"
    filepath = os.path.join(POSTS_DIR, filename)

    # use Unsplash for image
    image_url = f"https://source.unsplash.com/800x400/?{topic.replace(' ', ',')}"

    # save article HTML
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{topic}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <h1>{topic}</h1>
    <img src="../{image_url}" alt="{topic}" style="max-width:600px;"><br>
    {html_content}
</body>
</html>
""")

    # save metadata
    meta = {
        "title": topic,
        "filename": filename,
        "image": image_url,
        "content": html_content
    }

    meta_path = os.path.join(POSTS_DIR, f"{timestamp}.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)
    generate_post()
