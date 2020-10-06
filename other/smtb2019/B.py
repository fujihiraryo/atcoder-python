N = int(input())


def ans(N):
    for X in range(1, N + 1):
        if int(X * 1.08) == N:
            return X
    return ":("


print(ans(N))
