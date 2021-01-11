n = int(input())
(*a,) = map(int, input().split())
a = [(a[i], i) for i in range(2 ** n)]
while len(a) > 2:
    b = [max(a[2 * i], a[2 * i + 1]) for i in range(len(a) // 2)]
    a = b
print(min(a)[1] + 1)
