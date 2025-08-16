html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <article class="post">
        <header class="post-header">
            <h1>{title}</h1>
            <img src="{cover_image}" alt="{title}" loading="lazy">
        </header>
        <section class="post-content">
            <p>{intro}</p>
            {body}
            <p><strong>Conclusion:</strong> {conclusion}</p>
        </section>
    </article>
</body>
</html>"""

