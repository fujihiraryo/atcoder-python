import numpy as np

S = input()
L = []
N = len(S)

if S[-1] == '<':
    S += '><'
else:
    S += '<>'

index = 0
for n in range(N+1):
    if S[n: n + 2] == '><':
        L.append(S[index: n + 1])
        index = n + 1


def calc(string):
    K = len(string)
    c = K
    for k in range(K - 1):
        if string[k: k + 2] == '<>':
            c = k + 1
            break
    a = min(c, K - c)
    b = max(c, K - c)
    return a * (a - 1) // 2 + b * (b + 1) // 2


ans = 0
for string in L:
    ans += calc(string)

print(ans)
