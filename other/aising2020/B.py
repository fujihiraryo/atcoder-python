n = int(input())
*A, = map(int, input().split())
cnt = 0
for i in range(n):
    if (i + 1) % 2 == 1 and A[i] % 2 == 1:
        cnt += 1
print(cnt)
