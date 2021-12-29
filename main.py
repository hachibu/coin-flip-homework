import plotly.express as px
from util import run_trial, run_trials
from jinja2 import Template

titles = []
trials = (
    (1, 100),
    (2, 1000),
    (3, 10000),
    (4, 100000),
)
for (x, y) in trials:
    title="Trial #{} ({} flips)".format(x, y)
    titles.append(title)
    fig = px.line(run_trial(y), x="x", y="y", title=title)
    fig.write_html("docs/{}.html".format(title))

experiments = (
    (1, 100, 1000),
    (2, 1000, 1000),
)
for (x, y, z) in experiments:
    title = "Experiment #{} ({} trials of {} flips)".format(x, y, z)
    titles.append(title)
    fig = px.line(run_trials(y, z), x="x", y="y", title=title)
    fig.write_html("docs/{}.html".format(title))

template = Template("""
<!DOCTYPE html>
<html>
<head>
    <title>Coin Flip Homework</title>
</head>
<body>
    {% for title in titles %}
        <li><a href="{{ title | urlencode }}.html">{{ title }}</a></li>
    {% endfor %}
</body>
</html>
""")
template.stream(titles=titles).dump("docs/index.html")

