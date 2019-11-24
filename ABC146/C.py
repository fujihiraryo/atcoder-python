A, B, X = map(int, input().split())


def d(N):
    if N == 0:
        return 0
    else:
        return len(str(N))


def can_buy(N):
    return A * N + B * d(N) <= X


left = 0
right = 10 ** 9+1
while left < right - 1:
    mid = (left + right) // 2
    if can_buy(mid):
        left = mid
    else:
        right = mid
print(left)
