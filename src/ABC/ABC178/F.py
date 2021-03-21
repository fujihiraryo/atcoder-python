n = int(input())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())
a_last = [None] * (n + 1)
for i in range(n):
    a_last[a[i]] = i
b_first = [None] * (n + 1)
for i in range(n):
    if b_first[b[i]] is None:
        b_first[b[i]] = i
k = 0
for i in range(n + 1):
    if a_last[i] is None or b_first[i] is None:
        continue
    k = max(k, a_last[i] - b_first[i] + 1)
c = [b[(i - k) % n] for i in range(n)]
if all(a[i] != c[i] for i in range(n)):
    print("Yes")
    print(*c)
else:
    print("No")
