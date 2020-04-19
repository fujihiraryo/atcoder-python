n, m, c = map(int, input().split())
*B, = map(int, input().split())
cnt = 0
for i in range(n):
    *A, = map(int, input().split())
    if sum([A[j]*B[j] for j in range(m)])+c > 0:
        cnt += 1
print(cnt)
