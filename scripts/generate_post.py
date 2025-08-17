# scripts/generate_post.py
# ... generovanie title, intro, body, conclusion, image ...

html_content = f"""
<html>
<head>
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <div class="post-header">
    <h1>{title}</h1>
    <img src="{image}" alt="Cover Image" class="post-cover">
  </div>

  <div class="post-content">
    <p>{intro}</p>
    <hr>
    <p>{body}</p>
    <hr>
    <p>{conclusion}</p>
  </div>
</body>
</html>
"""

# uložiť do posts/{filename}.html
with open(f"posts/{filename}.html", "w", encoding="utf-8") as f:
    f.write(html_content)

