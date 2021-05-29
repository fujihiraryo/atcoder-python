MAGIC = 0.6180339887498948


def call(x):
    global n, memo
    if x == n + 1 or x == 0:
        return -1
    if memo[x] == -1:
        print(f"? {x}", flush=True)
        y = int(input())
        memo[x] = y
    return memo[x]


for _ in range(int(input())):
    n = int(input())
    memo = [-1] * (n + 2)
    # full search
    if n <= 15:
        ans = 0
        for x in range(1, n + 1):
            ans = max(ans, call(x))
        print(f"! {ans}", flush=True)
        continue
    # golden section search
    i, j = 0, n + 1
    x = j - round((j - i) * MAGIC)
    y = i + round((j - i) * MAGIC)
    while x < y:
        if call(x) < call(y):
            i = x
            x = y
            y = j - round((j - x) * MAGIC)
        else:
            j = y
            y = x
            x = i + round((y - i) * MAGIC)
    ans = call(x)
    print(f"! {ans}", flush=True)
