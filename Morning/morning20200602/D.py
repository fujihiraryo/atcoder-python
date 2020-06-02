def generate(n):
    if n == 1:
        for i in range(1, 10):
            yield [i]
    else:
        for A in generate(n - 1):
            for i in range(10):
                if abs(A[-1] - i) <= 1:
                    yield A + [i]


L = []
for n in range(1, 11):
    for A in generate(n):
        L.append(int(''.join([str(a) for a in A])))
k = int(input())
print(L[k - 1])
