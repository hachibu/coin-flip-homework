from util import run_trial, build_chart_html

trials = [100, 1000, 10000, 100000]
for i, n in enumerate(trials):
    build_chart_html(
        "trial-{}-{}-flips".format(i, n),
        run_trial(n))

