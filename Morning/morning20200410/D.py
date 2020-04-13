n = int(input())
AB = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort(key=lambda x: x[0]+x[1], reverse=True)
A, B = [], []
for i in range(n):
    a, b = AB[i]
    if i % 2 == 0:
        A.append(a)
    else:
        B.append(b)
print(sum(A)-sum(B))
