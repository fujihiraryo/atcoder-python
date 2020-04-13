import math
k = int(input())
x = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            x += math.gcd(math.gcd(a, b), c)
print(x)
