import os
import requests
from datetime import datetime

# Nastavenie cesty, kam sa uložia obrázky
IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)

# Funkcia na stiahnutie obrázka z Unsplash podľa témy
def fetch_unsplash_image(topic="ai"):
    url = f"https://source.unsplash.com/600x400/?{topic}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.url  # použijeme URL priamo pre blog/post
    else:
        raise Exception(f"Nepodarilo sa načítať obrázok z Unsplash: {response.status_code}")

# Generovanie príspevku
def generate_post():
    topic = "ai"  # tu môžeš dynamicky meniť tému
    image_url = fetch_unsplash_image(topic)
    
    # Tu si môžeš spraviť aj text príspevku, titulok atď.
    title = f"Nový článok o {topic}"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    post = {
        "title": title,
        "date": date,
        "image": image_url,
        "content": f"Toto je obsah článku o {topic}. Obrázok je od Unsplash."
    }
    
    # Uloženie príspevku ako JSON alebo inak podľa potreby
    post_path = f"posts/{title.replace(' ', '_')}.json"
    os.makedirs("posts", exist_ok=True)
    with open(post_path, "w", encoding="utf-8") as f:
        import json
        json.dump(post, f, ensure_ascii=False, indent=4)
    
    print(f"Post vytvorený: {post_path}")
    print(f"Obrázok: {image_url}")

if __name__ == "__main__":
    generate_post()
