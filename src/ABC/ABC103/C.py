n = int(input())
(*a,) = map(int, input().split())
print(sum(a[i] - 1 for i in range(n)))
