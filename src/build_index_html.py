from jinja2 import Environment, FileSystemLoader
import os

template_path = "{}/templates".format(os.path.abspath(os.path.dirname(__file__)))
env = Environment(loader=FileSystemLoader(template_path))
template = env.get_template('index.html')
docs_path = "docs"
index_html_path = "{}/index.html".format(docs_path)
html_files = []

for path in os.listdir(docs_path):
    if path.endswith('.html') and path != 'index.html':
        html_files.append(path)

html_files.sort()

template.stream(files=html_files).dump(index_html_path)
print("generated \"{}\"".format(index_html_path))
          
