N = int(input())
V = list(map(int, input().split()))
V.sort()
for n in range(N - 1):
    a = V.pop(0)
    b = V.pop(0)
    V.insert(0, (a + b) / 2)
print(V[0])
