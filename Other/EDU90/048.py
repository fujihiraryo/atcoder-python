n, k = map(int, input().split())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append(b)
    lst.append(a - b)
lst.sort(reverse=True)
print(sum(lst[:k]))
