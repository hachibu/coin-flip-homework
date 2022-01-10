from collections import Counter
import pandas as pd
import random

def div(a, b):
    precision = 3
    return round(a / b, precision)

def run_trial(n_flips):
    data = []
    n_heads = 0
    for n in range(1, n_flips + 1):
        if random.randrange(0, 2) == 0:
            n_heads += 1
        x = n
        y = div(n_heads, n)
        data.append((x, y))
    return pd.DataFrame(data, columns = ['# flips', '% heads'])

def run_experiment(n_trials, n_flips):
    results = []
    for n in range(1, n_trials + 1):
        t = run_trial(n_flips)
        x = t.iloc[-1, 1] * n_flips
        results.append(x)
    tally = list(Counter(results).items())
    tally.sort()
    data = []
    for (k, v) in tally:
        x = k
        y = div(v, n_trials)
        data.append((x, y))
    return pd.DataFrame(data, columns = ['# heads', '% observed'])

