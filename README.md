# Faceless AI Site (Auto Blog)

This repo auto-publishes one new article per day with a relevant Unsplash image.

## Quick start (super simple)
1) Upload this whole folder to your GitHub repo **2a0g0h2/faceless-ai-site** on branch `main`.
2) No extra setup needed — GitHub Actions is preconfigured and will run daily.
3) Connect this repo to **Cloudflare Pages** (Build command: none, Output directory: `/`).
4) Done. Every day, a new post appears automatically.

### Notes
- To change posting time: edit `.github/workflows/daily_post.yml` (the `cron` line).
- To tweak topics or formatting: edit `scripts/generate_post.py`.
