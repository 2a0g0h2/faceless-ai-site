import os
import random
import datetime
import requests
import subprocess

POSTS_DIR = "../posts"

# 📌 Funkcia na získanie náhodného obrázka z Unsplash
def get_random_image():
    keywords = ["technology", "ai", "future", "digital", "cyber", "virtual"]
    query = random.choice(keywords)
    url = f"https://source.unsplash.com/800x400/?{query}"
    return url

# 📌 Funkcia na generovanie článku
def generate_post():
    # názov a dátum
    title = "AI Trends " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    slug = title.lower().replace(" ", "-").replace(":", "")
    filename = f"{POSTS_DIR}/{slug}.html"

    # obrázok
    cover_image = get_random_image()

    # článok (jednoduchý text na ukážku, môže sa rozšíriť o AI generovanie obsahu)
    paragraphs = [
        "Artificial Intelligence (AI) is evolving at an unprecedented pace. Companies and researchers worldwide are exploring new ways to apply machine learning, automation, and neural networks to solve real-world problems.",
        "One of the biggest trends is the integration of AI into everyday life – from smart assistants to autonomous vehicles and advanced healthcare solutions.",
        "As technology advances, ethical questions become more pressing. Discussions around privacy, bias, and the potential risks of AI are shaping how societies adapt to this powerful tool.",
        "Looking ahead, AI is expected to play a central role in reshaping industries, economies, and the way humans interact with machines."
    ]

    content = "\n".join([f"<p>{p}</p>" for p in paragraphs])

    # HTML šablóna článku
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
        <img src="{cover_image}" alt="cover image" class="cover">
        {content}
    </article>
</body>
</html>"""

    # uloženie súboru
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Článok uložený: {filename}")
    return {
        "title": title,
        "date": date,
        "filename": filename,
        "excerpt": paragraphs[0],
        "cover_image": cover_image
    }

# 📌 Hlavný program
def main():
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)

    post_data = generate_post()

    # hneď po vygenerovaní spusti update_index.py
    try:
        subprocess.run(["python3", "scripts/update_index.py"], check=True)
        print("✅ Index bol úspešne aktualizovaný 🚀")
    except Exception as e:
        print(f"❌ Chyba pri aktualizácii indexu: {e}")

if __name__ == "__main__":
    main()
