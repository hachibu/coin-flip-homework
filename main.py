from util import run_trial, run_trials, gen_chart_html, gen_index_html

titles = []

trials = [100, 1000, 10000, 100000]
for i, n in enumerate(trials):
    title = "trial-{}-{}-flips".format(i, n)
    titles.append(title)
    gen_chart_html(title, run_trial(n))

experiments = [(100, 1000), (1000, 1000)]
for i, (n, m) in enumerate(experiments):
    title = "experiment-{}-{}-trials-of-{}-flips".format(i, n, m)
    titles.append(title)
    gen_chart_html(title, run_trials(n, m))

gen_index_html(titles)

