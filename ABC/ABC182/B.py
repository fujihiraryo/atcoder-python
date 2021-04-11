n = int(input())
(*A,) = map(int, input().split())
max_cnt = 0
ans = 2
for k in range(2, max(A) + 1):
    cnt = 0
    for a in A:
        if a % k == 0:
            cnt += 1
    if cnt > max_cnt:
        ans = k
        max_cnt = cnt
print(ans)
