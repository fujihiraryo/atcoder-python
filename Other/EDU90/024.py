n, k = map(int, input().split())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())
s = sum(abs(a[i] - b[i]) for i in range(n))
if s % 2 == k % 2 and s <= k:
    print("Yes")
else:
    print("No")
