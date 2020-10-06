import itertools

n, m, q = map(int, input().split())
X = [tuple(map(int, input().split())) for i in range(q)]
ans = 0
for A in itertools.combinations_with_replacement(range(m), n):
    tmp = 0
    for a, b, c, d in X:
        if A[b - 1] - A[a - 1] == c:
            tmp += d
    ans = max(ans, tmp)
print(ans)
