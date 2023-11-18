n, m = map(int, input().split())
s = input()
t = input()
lst = []
for i in range(m):
    for j in range(m):
        lst.append(t[: i + 1] + t[j:])
print(lst)
for i in range(n):
    for x in lst:
        s = s.replace(x, "#" * len(x))
print(s.split("#"))
