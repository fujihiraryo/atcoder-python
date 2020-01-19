def gcd(a, b):
    while b:
        a, b = b, a % b
    return gcd(a, b)


print(gcd(1000000, 99999))
