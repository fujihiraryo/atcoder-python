import bisect


def count_lower(A, x):
    # Aの要素のうちxより小さいものの個数
    return bisect.bisect_left(A, x)


def count_higher(A, x):
    # Aの要素のうちxより大きいものの個数
    return len(A)-bisect.bisect_right(A, x)


def count_pair(A, x):
    # A内のペアで積がxより小さいものの個数
    N = len(A)
    cnt = 0
    cnt_ = 0
    for n in range(N - 1):
        if A[n] < 0:
            y = x // A[n]
            # n+1番以降でyより大きいものの個数
            cnt += count_higher(A[n + 1:], y)
        elif A[n] > 0:
            y = -(-x // A[n])
            # n+1番以降でyより小さいものの個数
            cnt += count_lower(A[n + 1:], y)
        else:  # A[n]==0
            if x > 0:
                cnt += N - n - 1
        for m in range(n + 1, N):
            if A[n] * A[m] < x:
                cnt_ += 1
        if n == 24:
            print(y, A[n+1:])
    return cnt


def count_ans(A, x):
    # A内のペアで積がxより小さいものの個数
    N = len(A)
    cnt = 0
    B = [A[i] * A[j] for i in range(N - 1) for j in range(i + 1, N)]
    B.sort()
    return count_lower(B, x)


* A, = map(int, input().split())
x = int(input())
A.sort()
print(A)
print(count_pair(A, x), count_ans(A, x))

A = [-1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]
print(count_lower(A, 3.0))
print(count_higher(A, 3.0))
