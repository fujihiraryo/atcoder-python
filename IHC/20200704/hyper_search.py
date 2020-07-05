from random import choice
from time import time
from optimizer import Optimizer


def experiment(C, S, temp, threp, interval):
    opt = Optimizer(C, S)
    opt.optimize(temp, threp, interval, time())
    return opt.calc_score()


patterns = []
for temp in (600, 1000, 2000):
    for threp in (0.6, 0.8):
        for interval in (1, 26, 52):
            patterns.append((temp, threp, interval))

for ex in range(3):
    scores = []
    C = [choice(range(100)) for j in range(26)]
    S = [[choice(range(20000)) for j in range(26)] for i in range(365)]
    for i, (temp, threp, interval) in enumerate(patterns):
        scores.append(
            ((temp, threp, interval), experiment(
                C, S, temp, threp, interval)))
    scores.sort(key=lambda _: _[1], reverse=True)
    print(*scores[:5], sep="\n")
