n, x = map(int, input().split())
(*s,) = map(int, input().split())
print(sum(y for y in s if y <= x))
