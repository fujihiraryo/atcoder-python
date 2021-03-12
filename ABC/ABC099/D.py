from itertools import permutations

n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(m)]
c = [list(map(int, input().split())) for _ in range(n)]
cnt = [[0] * 3 for _ in range(m)]
sum_cnt = [0] * 3
for i in range(n):
    for j in range(n):
        cnt[c[i][j] - 1][(i + j) % 3] += 1
        sum_cnt[(i + j) % 3] += 1
min_cost = 10 ** 30
for color in permutations(range(m), 3):
    cost = 0
    for i in range(m):
        for j in range(3):
            cost += d[i][color[j]] * cnt[i][j]
    min_cost = min(min_cost, cost)
print(min_cost)
