from util import run_trial, build_chart_html

trials = [10, 100, 1000]

for i, n in enumerate(trials):
    build_chart_html(
        run_trial(n),
        "trial-{}-{}-flips".format(i, n))

