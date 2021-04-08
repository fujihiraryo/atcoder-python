n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
b = [0] * n
for i in range(n - 1):
    if i % 2:
        b[i] += 1
        b[i + 1] -= 1
    else:
        b[i] -= 1
        b[i + 1] += 1
b.sort()
ans0 = sum(a[i] * b[i] for i in range(n))
ans1 = sum(-a[i] * b[n - 1 - i] for i in range(n))
print(max(ans0, ans1))
