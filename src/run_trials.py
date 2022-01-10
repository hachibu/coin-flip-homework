from util import run_trial
import plotly.express as px

trials = [10, 100, 1000]

for i, n in enumerate(trials):
    df = run_trial(n)
    title = "trial-{}-{}-flips".format(i, n)
    path = "docs/{}.html".format(title)
    fig = px.bar(df, title=title, x="# flips", y="% heads")
    fig.write_html(path)
    print("generated \"{}\"".format(path))

