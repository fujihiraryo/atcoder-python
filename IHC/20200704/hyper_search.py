from random import choice
from time import time
from optimizer import Optimizer


def experiment(C, S, temp, threp, interval):
    opt = Optimizer(C, S)
    opt.optimize(temp, threp, interval, time())
    return opt.calc_score()


patterns = []
for temp in range(200, 1000, 200):
    for threp in (0.2, 0.4, 0.6, 0.8):
        for interval in range(1, 26 + 1, 5):
            patterns.append((temp, threp, interval))

for ex in range(50):
    scores = [0] * len(patterns)
    C = [choice(range(100)) for j in range(26)]
    S = [[choice(range(20000)) for j in range(26)] for i in range(365)]
    for i, (temp, threp, interval) in enumerate(patterns):
        scores[i] += experiment(C, S, temp, threp, interval)

for pattern, score in zip(patterns, scores):
    print(pattern, score)
