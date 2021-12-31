from util import run_trial, build_chart_html

trials = [100, 1000, 10000]

for i, n in enumerate(trials):
    build_chart_html(
        run_trial(n),
        "trial-{}-{}-flips".format(i, n))

