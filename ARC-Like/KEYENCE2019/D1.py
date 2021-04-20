MOD = 10 ** 9 + 7
n, m = map(int, input().split())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())
a_cnt = [0] * (n * m + 1)
for i in range(n):
    a_cnt[a[i]] += 1
b_cnt = [0] * (n * m + 1)
for j in range(m):
    b_cnt[b[j]] += 1
a_tmp, b_tmp = 0, 0
ans = 1
for x in range(1, n * m + 1)[::-1]:
    a_tmp += a_cnt[x]
    b_tmp += b_cnt[x]
    if a_cnt[x] > 1 or b_cnt[x] > 1:
        ans *= 0
    elif a_cnt[x] == 1 and b_cnt[x] == 0:
        ans *= b_tmp
    elif a_cnt[x] == 0 and b_cnt[x] == 1:
        ans *= a_tmp
    elif a_cnt[x] == 0 and b_cnt[x] == 0:
        ans *= a_tmp * b_tmp - n * m + x
    ans %= MOD
print(ans)
