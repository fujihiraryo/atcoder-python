def call(i):
    global n, a
    if i == 0 or i > n:
        return -1
    if a[i] == -1:
        print(f"? {i}", flush=True)
        a[i] = int(input())
    return a[i]


for _ in range(int(input())):
    n = int(input())
    f = [0, 610, 987, 1597]
    a = [-1] * (f[3] + 1)
    while f[3] - f[0] > 2:
        if call(f[1]) >= call(f[2]):
            f[2], f[3] = f[1], f[2]
            f[1] = f[0] + f[3] - f[2]
        else:
            f[0], f[1] = f[1], f[2]
            f[2] = f[0] + f[3] - f[1]
    print(f"! {a[f[1]]}", flush=True)
