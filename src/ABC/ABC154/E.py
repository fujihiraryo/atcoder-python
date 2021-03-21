def f(N, K):
    M, R = N // 10, N % 10
    if K == 0:
        return 1
    elif M == 0 and K == 1:
        return R
    elif M == 0 and K != 1:
        return 0
    else:
        return R * f(M, K - 1) + (9 - R) * f(M - 1, K - 1) + f(M, K)


N = int(input())
K = int(input())
print(f(N, K))
