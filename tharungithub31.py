
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Demo of Title and Anchor Tags</title>
</head>
<body>
    <h1>Welcome to My Demo Blog</h1>
    <p>This is a paragraph demonstrating an <a href="https://www.example.com" title="Example Website">anchor tag</a>.</p>
    <p>Click the link above to visit the example website.</p>
</body>
</html>
"""
with open("demo_blog.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file 'demo_blog.html' generated successfully.")
