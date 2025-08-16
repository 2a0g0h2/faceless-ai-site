import os
import json
import random
import datetime

# ---- Nastavenia tém a obrázkov ----
topics = [
    {
        "title": "The Future of Artificial Intelligence",
        "image": "https://source.unsplash.com/featured/?artificial-intelligence"
    },
    {
        "title": "Sustainable Energy and Green Tech",
        "image": "https://source.unsplash.com/featured/?green-energy"
    },
    {
        "title": "The Rise of Space Exploration",
        "image": "https://source.unsplash.com/featured/?space"
    },
    {
        "title": "How AI is Transforming Healthcare",
        "image": "https://source.unsplash.com/featured/?healthcare"
    },
    {
        "title": "The Impact of Blockchain on Business",
        "image": "https://source.unsplash.com/featured/?blockchain"
    },
]

def generate_article(topic):
    """Vygeneruje falošný článok (500–1000 slov) s úvodom, bodmi a záverom."""
    paragraphs = []
    
    intro = (
        f"{topic['title']} is one of the hottest topics today. "
        f"In this article, we will explore the key ideas, trends, and challenges shaping this area."
    )
    paragraphs.append(intro)

    body_points = [
        "Background and context of the topic.",
        "Current trends shaping the field.",
        "Key opportunities and innovations.",
        "Challenges and obstacles to overcome.",
        "Future outlook and predictions."
    ]

    for point in body_points:
        text = (
            f"### {point}\n\n"
            f"This section discusses {point.lower()} in detail. "
            f"Examples, case studies, and real-world applications are highlighted to give readers "
            f"a clear picture of why this matters today and what it means for tomorrow."
        )
        paragraphs.append(text)

    conclusion = (
        "### Conclusion\n\n"
        f"In summary, {topic['title']} continues to evolve rapidly. "
        "By understanding the trends, challenges, and opportunities, "
        "individuals and businesses can prepare for the future with confidence."
    )
    paragraphs.append(conclusion)

    # zopakujeme text, aby mal rozsah 500–1000 slov
    content = "\n\n".join(paragraphs * 2)
    return content


def main():
    today = datetime.date.today().isoformat()
    topic = random.choice(topics)

    article_content = generate_article(topic)

    # pripraviť meta
    post = {
        "title": topic["title"],
        "date": today,
        "image": topic["image"],
        "excerpt": article_content.split(".")[0] + "...",
        "content": article_content
    }

    # súbory
    base_filename = f"posts/{today}-{topic['title'].lower().replace(' ', '-')}"
    os.makedirs("posts", exist_ok=True)

    with open(base_filename + ".json", "w") as f:
        json.dump(post, f, indent=2)

    with open(base_filename + ".md", "w") as f:
        f.write(f"# {post['title']}\n\n![Cover Image]({post['image']})\n\n{article_content}")

    with open(base_filename + ".html", "w") as f:
        f.write(f"""
<html>
  <head><title>{post['title']}</title></head>
  <body>
    <h1>{post['title']}</h1>
    <img src="{post['image']}" style="max-width:100%;border-radius:12px;" />
    <article>{article_content}</article>
  </body>
</html>
        """)

if __name__ == "__main__":
    main()

