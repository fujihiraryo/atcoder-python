n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab.append(min((a - b) % (2 * n), (b - a) % (2 * n)))
ab.sort()

if any(d % 2 == 0 for d in ab):
    print("Yes")
else:
    print("No")
