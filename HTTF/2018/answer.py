import random
import sys
import time

n = 100
q = 1000
A = [list(map(int, input().split())) for i in range(n)]


def generate():
    x = random.choice(range(n))
    y = random.choice(range(n))
    h = random.choice(range(n)) + 1
    return x, y, h


def evaluate(A, B):
    score = 2 * 10 ** 8
    for i in range(n):
        for j in range(n):
            score -= abs(A[i][j] - B[i][j])
    return score


def update(B, xyh, inverse=False):
    x, y, h = xyh
    for i in range(n):
        for j in range(n):
            sand = max(0, h - abs(i - x) - abs(j - y))
            if inverse:
                B[i][j] -= sand
            else:
                B[i][j] += sand


start = time.time()
ans = [generate() for _ in range(q)]
B = [[0] * n for i in range(n)]
for xyh in ans:
    update(B, xyh)
max_score = evaluate(A, B)
loop_cnt = 0
while time.time() - start < 5.5:
    idx = random.choice(range(q))
    before = ans[idx]
    after = generate()
    update(B, before, inverse=True)
    update(B, after)
    score = evaluate(A, B)
    if score > max_score:
        ans[idx] = after
        max_score = score
    else:
        update(B, before)
        update(B, after, inverse=True)
    loop_cnt += 1
print(loop_cnt, file=sys.stderr)

print(q)
for x, y, h in ans:
    print(x, y, h)
