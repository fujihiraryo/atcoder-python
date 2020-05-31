n = int(input())
*A, = map(int, input().split())
A.sort()
ans = 1
for i in range(n):
    ans *= A[i]
    if ans > 10**18:
        print(-1)
        exit()
print(ans)
