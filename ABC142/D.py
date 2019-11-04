def factor(n):
    factor_set = {1}
    tmp = int(n**0.5)+1
    for i in range(2, tmp):
        while n % i == 0:
            n = n // i
            factor_set.add(i)
    factor_set.add(n)
    return factor_set


A, B = map(int, input().split())

print(len(factor(A) & factor(B)))
