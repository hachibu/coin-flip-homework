from util import run_experiment, build_chart_html

experiments = [
    (1000, 10),
    (1000, 100),
    (1000, 1000),
    (10000, 10),
    (10000, 100),
    (10000, 10000),
]

for i, (n, m) in enumerate(experiments):
    build_chart_html(
        run_experiment(n, m),
        "experiment-{}-{}-trials-of-{}-flips".format(i, n, m),
        [0, 1])

