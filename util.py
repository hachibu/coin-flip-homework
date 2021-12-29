import pandas as pd
import random
from jinja2 import Template

def run_trial(n_flips):
    data = []
    n_heads = 0
    for n in range(1, n_flips + 1):
        if random.randrange(0, 2) == 0:
            n_heads += 1
        data.append((n, round(n_heads / n, 3)))
    return pd.DataFrame(data, columns = ['x', 'y'])

def run_trials(n_trials, n_flips):
    data = []
    for n in range(1, n_trials + 1):
        df = run_trial(n_flips)
        data.append((n, df.iloc[-1, 1]))
    return pd.DataFrame(data, columns = ['x', 'y'])

def gen_index_html(titles):
    template = Template("""
<!DOCTYPE html>
<html>
<head>
    <title>Coin Flip Homework</title>
</head>
<body>
    <ul>
        {% for title in titles %}
            <li><a href="{{ title | urlencode }}.html">{{ title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
    """)
    template.stream(titles=titles).dump("docs/index.html")

