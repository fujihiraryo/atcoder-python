# 各部分の合計がK以下になるようにリストを分割する回数の最小値
N, K = map(int, input().split())
*A, = map(int, input().split())
l, r = 0, A[0]
cnt = 0
for i in range(1, N):
    l, r = r, r + A[i]
    print(l, r)
    if l <= K and r > K:
        cnt += 1
        l, r = 0, A[i]
    if r > K:
        print('-1')
        exit()
print(cnt)