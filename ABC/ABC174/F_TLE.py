n, q = map(int, input().split())
*C, = map(int, input().split())
k = 2**19
S = [set()] * (2 * k - 1)
for i in range(n):
    S[k - 1 + i] = {C[i]}
for i in range(k - 1)[::-1]:
    S[i] = S[2 * i + 1] | S[2 * i + 2]
for _ in range(q):
    x, y = map(int, input().split())
    x, y = x + k - 2, y + k - 1
    ans = set()
    while x < y:
        if x % 2 == 0:
            ans |= S[x]
            x += 1
        if y % 2 == 0:
            y -= 1
            ans |= S[y]
        x, y = (x - 1) // 2, (y - 1) // 2
    # print(len(ans))
