from random import choice
from random import random
from time import time


class Optimizer:
    def __init__(self, C, S):
        self.C = C
        self.S = S
        X = []
        L = [-1] * 26
        for i in range(365):
            max_diff = -10**10
            best_j = 0
            for j in range(26):
                memo = L[j]
                L[j] = i
                diff = self.S[i][j] - \
                    sum([self.C[jj] * (i - L[jj]) for jj in range(26)])
                if diff > max_diff:
                    max_diff = diff
                    best_j = j
                L[j] = memo
            L[best_j] = i
            X.append(best_j)
        self.X = X

    def calc_score(self):
        score = 0
        L = [-1 for j in range(26)]
        A = [0 for j in range(26)]
        for i in range(365):
            score += self.S[i][self.X[i]]
            A[self.X[i]] += (i - L[self.X[i]]) * \
                (i - L[self.X[i]] - 1) // 2
            L[self.X[i]] = i
        for j in range(26):
            A[j] += (365 - L[j]) * (365 - L[j] - 1) // 2
            score -= self.C[j] * A[j]
        return score

    def optimize(self, temp, threp, interval, start_time, lim=1.8):
        max_score = self.calc_score()
        while True:
            t = (time() - start_time) / 2
            if random() < threp:
                i = choice(range(365))
                j = choice(range(26))
                memo = self.X[i]
                self.X[i] = j
                new_score = self.calc_score()
                if new_score > max_score:
                    max_score = new_score
                elif random() < pow(2.7, (new_score - max_score) / pow(2000, 1 - t)):
                    max_score = new_score
                else:
                    self.X[i] = memo
            else:
                a = choice(range(interval))
                i0 = choice(range(365 - a))
                i1 = i0 + a
                self.X[i0], self.X[i1] = self.X[i1], self.X[i0]
                new_score = self.calc_score()
                if new_score > max_score:
                    max_score = new_score
                elif random() < pow(2.7, (new_score - max_score) / pow(2000, 1 - t)):
                    max_score = new_score
                else:
                    self.X[i0], self.X[i1] = self.X[i1], self.X[i0]
            if time() - start_time > lim:
                break
        return max(max_score + 10**6, 0)


if __name__ == "__main__":
    d = int(input())
    *C, = map(int, input().split())
    S = [list(map(int, input().split())) for i in range(d)]
    opt = Optimizer(C, S)
    opt.optimize(500, 0.7, 8, time())
    for x in opt.X:
        print(x + 1)
    # print(opt.calc_score())
