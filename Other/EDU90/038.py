from math import gcd

MAX = 10 ** 18
a, b = map(int, input().split())
g = gcd(a, b)
if a > MAX // ((b // g)):
    print("Large")
    exit()
ans = a * (b // g)
print(ans if ans <= MAX else "Large")
