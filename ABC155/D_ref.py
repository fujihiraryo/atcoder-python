import sys


def bisect_left(A, N, x):
    l, r = -1, N
    for _ in range(N):
        if r - l <= 1:
            return r
        m = (l + r) // 2
        if A[m] >= x:
            r = m
        else:
            l = m


def bisect_right(A, N, x):
    l, r = -1, N
    for _ in range(N):
        if r - l <= 1:
            return r
        m = (l + r) // 2
        if A[m] > x:
            r = m
        else:
            l = m


def count_pair(A, N, x):
    # A内のペアで積がxより小さいものの個数
    cnt = 0
    for n in range(N - 1):
        if A[n] < 0:
            y = x // A[n]
            # n+1番以降でyより大きいものの個数
            cnt += N - max(n + 1, bisect_right(A, N, y))
        elif A[n] > 0:
            y = -(-x // A[n])
            # n+1番以降でyより小さいものの個数
            cnt += max(n+1, bisect_left(A, N, y)) - (n + 1)
        elif x > 0:
            cnt += N - (n + 1)
    return cnt


def main():
    # count_pair(x)<Kをみたすxの最大値を求める
    N, K = map(int, sys.stdin.readline().split())
    * A, = map(int, sys.stdin.readline().split())
    A.sort()
    inf = 10**18+1
    l, r = -inf, inf
    for _ in range(inf):
        if r - l <= 1:
            print(l)
            exit()
        c = (l + r) // 2
        if count_pair(A, N, c) < K:
            l = c
        else:
            r = c


if __name__ == '__main__':
    main()
