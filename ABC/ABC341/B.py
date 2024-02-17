n = int(input())
(*a,) = map(int, input().split())
for i in range(n - 1):
    s, t = map(int, input().split())
    a[i + 1] += a[i] // s * t
print(a[n - 1])
