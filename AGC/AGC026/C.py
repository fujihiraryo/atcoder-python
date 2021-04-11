from collections import defaultdict

n = int(input())
s = input()
s0, s1 = s[:n], s[n : 2 * n][::-1]
map0 = defaultdict(int)
map1 = defaultdict(int)
for x in range(1 << n):
    a0, b0 = "", ""
    a1, b1 = "", ""
    for i in range(n):
        if (1 << i) & x:
            a0 += s0[i]
            a1 += s1[i]
        else:
            b0 += s0[i]
            b1 += s1[i]
    map0[(a0, b0)] += 1
    map1[(a1, b1)] += 1
ans = 0
for a, b in map0:
    ans += map0[(a, b)] * map1[(a, b)]
print(ans)
