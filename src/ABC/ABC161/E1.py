def work(S, k, c):
    tir = 0
    cnt = 0
    for i, s in enumerate(S):
        if s == "o" and tir == 0 and cnt < k:
            yield i
            tir = c
            cnt += 1
        else:
            tir = max(tir - 1, 0)


n, k, c = map(int, input().split())
S = list(input())
L = [i + 1 for i in work(S, k, c)]
R = [n - i for i in work(S[::-1], k, c)][::-1]
for l, r in zip(L, R):
    if l == r:
        print(l)
