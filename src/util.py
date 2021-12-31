from collections import Counter
import pandas as pd
import plotly.express as px
import random

def build_chart_html(dataframe, title, xaxes_range = None):
    path = "docs/{}.html".format(title)
    fig = px.line(dataframe, x="x", y="y", title=title)
    if xaxes_range is not None:
        fig.update_xaxes(range=xaxes_range)
    fig.write_html(path)
    print("generated \"{}\"".format(path))

def run_trial(n_flips):
    data = []
    n_heads = 0
    for n in range(1, n_flips + 1):
        if random.randrange(0, 2) == 0:
            n_heads += 1
        data.append((n, round(n_heads / n, 3)))
    return pd.DataFrame(data, columns = ['x', 'y'])

def run_experiment(n_trials, n_flips):
    results = []
    for n in range(1, n_trials + 1):
        results.append(run_trial(n_flips).iloc[-1, 1])
    data = list(Counter(results).items())
    data.sort()
    return pd.DataFrame(data, columns = ['x', 'y'])

