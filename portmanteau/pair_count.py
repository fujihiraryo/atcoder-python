def count_pair(A, c):
    # 積がc未満のペアを数える
    A.sort()
    A_minus = [a for a in A if a < 0]
    A_plus = [a for a in A if a > 0]
    N, N_minus, N_plus = len(A), len(A_minus), len(A_plus)
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
        if c == 1:
            print(cnt)
        # A_plusのペアで積がc以上のものの個数を数える
        j = N_plus - 1
        for i in range(N_plus - 1)[::-1]:
            while j >= i + 1 and A_plus[i] * A_plus[j] >= c:
                j -= 1
            cnt += N_plus - 1 - j
        if c == 1:
            print(cnt)
        cnt = N * (N - 1) // 2 - cnt
    return cnt


if __name__ == '__main__':
    A = [-2, -1, 0, 0, 1, 2, 3]
    N = len(A)
    print(sorted([A[i]*A[j] for i in range(N-1) for j in range(i+1, N)]))
    # for c in [-1, 0, 1, 2]:
    #     print(count_pair(A, c))
    count_pair(A, 1)
