from util import run_experiment, build_chart_html

experiments = [
    (100, 1000),
    (1000, 1000),
]

for i, (n, m) in enumerate(experiments):
    build_chart_html(
        run_experiment(n, m),
        "experiment-{}-{}-trials-of-{}-flips".format(i, n, m))

