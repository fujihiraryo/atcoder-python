def is_prime(x):
    for i in range(2, int(x**0.5)+2):
        if x % i == 0:
            return False
    return True


# n = 2**17
# for a in range(20000, 30000):
#     for w in range(2, 100):
#         p = a*n+1
#         if is_prime(p) and pow(w, n, p) == 1:
#             print(n, p, w)
#             exit()
p, w = 2662072321, 21
for i in range(1, 262144):
    if pow(w, i, p) == 1:
        print(i)
