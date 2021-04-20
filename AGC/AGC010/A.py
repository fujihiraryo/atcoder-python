n = int(input())
(*a,) = map(int, input().split())
cnt = 0
for i in range(n):
    if a[i] % 2:
        cnt += 1
if cnt % 2:
    print("NO")
else:
    print("YES")
