n, x = map(int, input().split())
(*a,) = map(int, input().split())
print(*[a[i] for i in range(n) if a[i] != x])
