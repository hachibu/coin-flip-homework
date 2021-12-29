import pandas as pd
import random

def run_trial(n_flips):
    data = []
    n_heads = 0
    for n in range(1, n_flips + 1):
        if random.randrange(0, 2) == 0:
            n_heads += 1
        data.append((n, round(n_heads / n, 3)))
    return pd.DataFrame(data, columns = ['x', 'y'])

def run_trials(n_trials, n_flips):
    data = []
    for n in range(1, n_trials + 1):
        df = run_trial(n_flips)
        data.append((n, df.iloc[-1, 1]))
    return pd.DataFrame(data, columns = ['x', 'y'])

