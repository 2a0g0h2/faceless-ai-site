import os
import json
import random
from datetime import datetime

# Cesty
POSTS_DIR = "../posts"
IMAGES_DIR = "../images"

# Náhodné témy a úvody
TOPICS = [
    "The Future of AI in Everyday Life",
    "Top 10 Productivity Hacks for Remote Workers",
    "Sustainable Living: Small Changes, Big Impact",
    "How to Invest Smartly in 2025",
    "Mindfulness Techniques for a Busy Mind"
]

EXCERPTS = [
    "Discover the latest trends and insights in this topic.",
    "Learn actionable tips to improve your daily routine.",
    "A guide to making smarter decisions and living sustainably.",
    "Investing strategies that can boost your financial future.",
    "Techniques to calm your mind and enhance focus."
]

# Funkcia pre náhodný obrázok
def get_random_image():
    imgs = [f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    if not imgs:
        return "default.jpg"
    return random.choice(imgs)

# Hlavná funkcia
def main():
    title = random.choice(TOPICS)
    excerpt = random.choice(EXCERPTS)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cover_image = get_random_image()
    
    # Body článku
    body = f"""
## Introduction
This article discusses "{title}" and provides key insights and practical advice.

## Main Content
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.

## Conclusion
In conclusion, staying informed and adopting best practices can greatly improve your results in this area.
"""

    # HTML obsah
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{excerpt}">
    <title>{title}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="post">
        <h1>{title}</h1>
        <p><em>{date}</em></p>
        <img src="../images/{cover_image}" alt="Cover image" style="max-width:600px; height:auto;">
        {body}
    </div>
</body>
</html>
"""

    # JSON obsah
    json_content = {
        "title": title,
        "date": date,
        "excerpt": excerpt,
        "cover_image": cover_image,
        "body": body
    }

    # Uloženie súborov
    safe_title = title.replace(" ", "_").replace("/", "_")
    os.makedirs(POSTS_DIR, exist_ok=True)
    
    with open(os.path.join(POSTS_DIR, f"{safe_title}.md"), "w") as f_md:
        f_md.write(body)
    
    with open(os.path.join(POSTS_DIR, f"{safe_title}.html"), "w") as f_html:
        f_html.write(html_content)
    
    with open(os.path.join(POSTS_DIR, f"{safe_title}.json"), "w") as f_json:
        json.dump(json_content, f_json, indent=4)

    print(f"Article '{title}' generated successfully!")

if __name__ == "__main__":
    main()
