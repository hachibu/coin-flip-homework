import os
from jinja2 import Template

template = Template("""
<!DOCTYPE html>
<html>
<head>
    <title>Coin Flip Homework</title>
</head>
<body>
    <ul>
        {% for file in files %}
            <li><a href="{{ file | urlencode }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
""")

index_html_path = "docs/index.html"
html_files = list(filter(
    lambda path: path.endswith('.html') and path != 'index.html',
    os.listdir("docs")))
html_files.sort()

template.stream(files=html_files).dump(index_html_path)
print("generated \"{}\"".format(index_html_path))
          
