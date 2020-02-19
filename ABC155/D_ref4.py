import bisect
N, K = map(int, input().split())
* A, = map(int, input().split())
A_plus = [a for a in A if a > 0]
A_minus = [a for a in A if a < 0]
A_plus.sort()
A_minus.sort()
N_minus = len(A_minus)
N_plus = len(A_plus)
N_zero = N-(N_minus+N_plus)

# (積がx未満のAのペアの個数)<Kをみたすxの最大値を求める
inf = 10**18+1
l, r = -inf, inf
while r - l > 1:
    c = (l + r) // 2
    # A内のペアで積がcより小さいものの個数を求める
    if c <= 0:
        # A_minusの各要素aに対してc/aより大きいA_plusの要素の個数を数える
        cnt = 0
        for a in A_minus:
            x = c // a
            cnt += N_plus - bisect.bisect_right(A_plus, x)
    else:
        # 積がc以上になる個数を求めて最後にN(N-1)/2からひく
        cnt = 0
        # A_minusの各要素aに対してc/a以下で, aより後のA_minusの要素の個数を数える
        for n, a in enumerate(A_minus):
            x = c // a
            cnt += bisect.bisect_right(A_minus, x, lo=n + 1) - (n + 1)
        # A_plusの各要素aに対してc/a以上で, aより後のA_plusの要素の個数を数える
        for n, a in enumerate(A_plus):
            x = -(-c // a)
            cnt += N_plus - bisect.bisect_left(A_plus, x, lo=n + 1)
        cnt = N * (N - 1) // 2 - cnt
    if cnt < K:
        l = c
    else:
        r = c
print(l)
