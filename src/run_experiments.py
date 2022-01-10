from util import run_experiment
import plotly.express as px

experiments = [
    (1000, 10),
    (1000, 100),
    (1000, 1000),
    (10000, 10),
    (10000, 100),
    (10000, 10000),
]

for i, (n, m) in enumerate(experiments):
    df = run_experiment(n, m)
    title = "experiment-{}-{}-trials-of-{}-flips".format(i, n, m)
    path = "docs/{}.html".format(title)
    fig = px.bar(df, title=title, x = "# heads", y = "% observed")
    fig.write_html(path)
    print("generated \"{}\"".format(path))

