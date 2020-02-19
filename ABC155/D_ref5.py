import bisect
N, K = map(int, input().split())
* A, = map(int, input().split())
A_minus = [a for a in A if a < 0]
A_plus = [a for a in A if a > 0]
A_minus.sort()
A_plus.sort()

N_minus = len(A_minus)
N_plus = len(A_plus)

# (積がx未満のAのペアの個数)<Kをみたすxの最大値を求める
inf = 10 ** 18 + 1
l, r = -inf, inf
while r - l > 1:
    c = (l + r) // 2
    # A内のペアで積がcより小さいものの個数を求める
    if c <= 0:
        cnt = 0
        # A_minusとA_plusの積でc未満の個数を数える
        j = N_plus - 1
        for i in range(N_minus)[::-1]:
            while j >= 0 and A_minus[i] * A_plus[j] < c:
                j -= 1
            cnt += N_plus - 1 - j
    else:
        cnt = 0
        # A_minusのペアで積がc以上のものの個数を数える
        j = N_minus - 1
        for i in range(N_minus - 1)[::-1]:
            while j >= i + 1 and A_minus[i] * A_minus[j] < c:
                j -= 1
            cnt += j - i - 1
        # A_plusのペアで積がc以上のものの個数を数える
        j = N_plus - 1
        for i in range(N_plus - 1)[::-1]:
            while j >= i + 1 and A_plus[i] * A_plus[j] >= c:
                j -= 1
            cnt += N_plus - 1 - j
        cnt = N * (N - 1) // 2 - cnt
    print(c, cnt)
    if cnt < K:
        l = c
    else:
        r = c
print(l)
