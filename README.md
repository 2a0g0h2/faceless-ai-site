# Faceless AI Site

Tento projekt automaticky generuje články pomocou AI a nasadzuje ich na web cez Hugo a Cloudflare Pages.

## Ako to spustiť

1. Vytvor si účet na GitHub a Cloudflare.
2. Na GitHube založ nové repo a nahraj tieto súbory.
3. V Cloudflare Pages prepoj repo, nastav Hugo build (`hugo`, output `public`).
4. GitHub Actions každý deň o 08:00 UTC spustí `generate_articles.py` a pridá nové články.

Úpravy:
- **data/keywords.csv** – pridaj svoje témy
- **data/affiliates.json** – pridaj svoje affiliate odkazy
