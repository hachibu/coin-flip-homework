import plotly.express as px
from util import run_trial, run_trials, gen_index_html

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

gen_index_html(titles)

