K, Q = map(int, input().split())
*D, = map(int, input().split())
for q in range(Q):
    n, x, m = map(int, input().split())
    D1 = [d % m for d in D]
    r = (n - 1) % K
    cnt_0 = D1.count(0) * ((n - 1) // K) + D1[:r].count(0)
    a = x
    # 第n-1項を求める
    b = a + sum(D1) * ((n - 1) // K) + sum(D1[:r])
    # 繰り上がりの回数
    cnt_p = b // m - a // m
    cnt_n = (n - 1) - cnt_0 - cnt_p
    print(cnt_n)
