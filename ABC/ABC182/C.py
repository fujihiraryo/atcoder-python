n = input()
k = len(n)
ans = k
for s in range(1, 1 << k):
    tmp = ""
    for i in range(k):
        if (1 << i) & s:
            tmp += n[i]
    if int(tmp) % 3 == 0:
        ans = min(ans, k - bin(s).count("1"))
if ans == k:
    print("-1")
else:
    print(ans)
