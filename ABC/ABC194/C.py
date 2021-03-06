n = int(input())
*a, = map(int, input().split())
s1, s2 = [0], [0]
for i in range(n):
    s1.append(s1[i] + a[i])
    s2.append(s2[i] + a[i] ** 2)
ans = 0
for i in range(1, n):
    ans += i * a[i] ** 2
    ans -= 2 * a[i] * s1[i]
    ans += s2[i]
print(ans)
