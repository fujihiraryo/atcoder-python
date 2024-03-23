n = int(input())
s = input()
(*c,) = map(int, input().split())

INF = 10**30
good0 = [INF] * (n + 1)
good1 = [INF] * (n + 1)
reach0 = [0] * (n + 1)
reach1 = [0] * (n + 1)

for i in range(n):
    reach0[i + 1] = reach1[i] + (c[i] if s[i] == "1" else 0)
    reach1[i + 1] = reach0[i] + (c[i] if s[i] == "0" else 0)

for i in range(1, n):
    good0[i + 1] = min(
        good1[i] + (c[i] if s[i] == "1" else 0),
        reach0[i] + (c[i] if s[i] == "1" else 0),
    )
    good1[i + 1] = min(
        good0[i] + (c[i] if s[i] == "0" else 0),
        reach1[i] + (c[i] if s[i] == "0" else 0),
    )

print(min(good0[n], good1[n]))
# print(good0)
# print(good1)
# print(reach0)
# print(reach1)
