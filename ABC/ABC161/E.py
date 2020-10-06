n, k, c = map(int, input().split())
S = list(input())


def f(S):
    L = []
    on = True
    cnt = 0
    for i in range(n):
        if not on:
            if cnt == c:
                on = True
            cnt += 1
        if on and S[i] == "o":
            on = False
            cnt = 0
            L.append(i)
            if len(L) == k:
                break
    return L


L = f(S)
R = [n - 1 - i for i in f(S[::-1])][::-1]
for i in range(k):
    if L[i] == R[i]:
        print(L[i] + 1)
