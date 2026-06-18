import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Legal Document</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body style="align-items: flex-start; padding-top: 3rem;">
    <div class="container container-legal">
        <h1>{app_name}</h1>
        <p class="subtitle">{document_type}</p>
        
        <div class="legal-content">{content}</div>
        
        <div class="button-group-row">
            <button onclick="window.close()" class="btn btn-secondary" style="min-width: 200px;">Close Tab</button>
        </div>
    </div>
</body>
</html>"""

files = [
    ('ppsadhguru.txt', 'sadhguru_pp.html', 'Wakeup with Sadhguru App', 'Privacy Policy'),
    ('tossadhguru.txt', 'sadhguru_tos.html', 'Wakeup with Sadhguru App', 'Terms of Service'),
    ('ppsetscounter.txt', 'setcounter_pp.html', 'Simple set counter and timer App', 'Privacy Policy'),
    ('tossetscounter.txt', 'setcounter_tos.html', 'Simple set counter and timer App', 'Terms of Service')
]

for txt_file, html_file, app, doc_type in files:
    if os.path.exists(txt_file):
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read().replace('<', '&lt;').replace('>', '&gt;')
        html = template.format(title=app, app_name=app, document_type=doc_type, content=content)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Created {html_file}")
    else:
        print(f"Error: {txt_file} not found")
