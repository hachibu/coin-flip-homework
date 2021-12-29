from util import run_trial, run_trials, gen_chart_html, gen_index_html

titles = []

trials = [100, 1000, 10000, 100000]
for x, y in enumerate(trials):
    title = "trial-{}-{}-flips".format(x, y)
    titles.append(title)
    gen_chart_html(title, run_trial(y))

experiments = [(100, 1000), (1000, 1000)]
for x, (y, z) in enumerate(experiments):
    title = "experiment-{}-{}-trials-of-{}-flips".format(x, y, z)
    titles.append(title)
    gen_chart_html(title, run_trials(y, z))

gen_index_html(titles)

