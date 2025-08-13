import csv
import json
import os
import random
from datetime import datetime

# Načítanie kľúčových slov
with open("data/keywords.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    keywords = list(reader)

# Načítanie affiliate odkazov
with open("data/affiliates.json", encoding="utf-8") as f:
    affiliates = json.load(f)

os.makedirs("content", exist_ok=True)

# Falošný AI generátor (public free AI endpoints simulované)
def fake_ai_generate(keyword, language):
    if language == "sk":
        return f"AI článok na tému '{keyword}'. Tento obsah bol vygenerovaný automaticky a obsahuje užitočné informácie."
    else:
        return f"AI article on the topic '{keyword}'. This content was generated automatically and contains useful information."

# Generovanie článkov
for kw in keywords:
    title = kw["keyword"].capitalize()
    lang = kw["language"]
    body = fake_ai_generate(kw["keyword"], lang)

    affiliate_box = "\n\n".join([
        f"### {a['name']}\n[{a['description']}]({a['link']})"
        for a in affiliates
    ])

    filename = f"{kw['keyword'].replace(' ', '-')}.md"
    with open(os.path.join("content", filename), "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: \"{title}\"\ndate: {datetime.utcnow().strftime('%Y-%m-%d')}\n---\n")
        f.write(body + "\n\n---\n\n" + affiliate_box)
