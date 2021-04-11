n = int(input())
A = set()
for i in range(1, int(n ** 0.5) + 3):
    if n % i == 0:
        A.add(i)
        A.add(n // i)
A = list(A)
A.sort()
for a in A:
    print(a)
