n = int(input())
lst = []
for _ in range(n):
    s, t = input().split()
    lst.append((int(t), s))
lst.sort()
print(lst[-2][1])
