n = int(input())
W = []
for i in range(n):
    a, b = map(int, input().split())
    W.append((a, b))
W.sort(key=lambda x: x[1])
x = 0
for i in range(n):
    a, b = W[i]
    x += a
    if x > b:
        print('No')
        exit()
print('Yes')
