def product(A, B):
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum([A[i][k]*B[k][j] for k in range(n)]) % p
    return C


def matpow(A, k):
    if k == 1:
        return A
    if k % 2 == 0:
        B = matpow(A, k//2)
        return product(B, B)
    return product(A, matpow(A, k-1))


n, k = map(int, input().split())
p = 10**9+7
A = [list(map(int, input().split())) for i in range(n)]
B = matpow(A, k)
print(sum([sum(B[i]) for i in range(n)]) % p)
