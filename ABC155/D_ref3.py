import bisect


def count_pair(A, x, K):
    # A内のペアで積がxより小さいものの個数がK未満ならTrueを返す
    cnt = 0
    N = len(A)
    for n in range(N - 1):
        if A[n] < 0:
            y = x // A[n]
            # n+1番以降でyより大きいものの個数
            cnt += N - max(n + 1, bisect.bisect_right(A, y))
            if cnt >= K:
                return False
        elif A[n] > 0:
            y = -(-x // A[n])
            # n+1番以降でyより小さいものの個数
            cnt += max(n + 1, bisect.bisect_left(A, y)) - (n + 1)
            if cnt >= K:
                return False
        elif x > 0:
            cnt += N - (n + 1)
            if cnt >= K:
                return False
    return True


def main():
    # count_pair(x)<Kをみたすxの最大値を求める
    N, K = map(int, input().split())
    * A, = map(int, input().split())
    A.sort()
    inf = 10**18+1
    l, r = -inf, inf
    for _ in range(inf):
        if r - l <= 1:
            print(l)
            exit()
        c = (l + r) // 2
        if count_pair(A, c, K):
            l = c
        else:
            r = c


if __name__ == '__main__':
    main()
