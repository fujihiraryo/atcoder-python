import itertools

a, b, c = map(int, input().split())
cnt = 0
for X in itertools.permutations(range(a + b + c)):
    X = list(X)
    Y = [[] for i in range(6)]
    Y[0] = X[0:a]
    Y[1] = X[a : a + b]
    Y[2] = X[a + b : a + b + c]
    for i in range(3):
        if i < a:
            Y[i + 3].append(Y[0][i])
        if i < b:
            Y[i + 3].append(Y[1][i])
        if i < c:
            Y[i + 3].append(Y[2][i])
    if all([Y[i] == sorted(Y[i]) for i in range(6)]):
        cnt += 1
print(cnt)
