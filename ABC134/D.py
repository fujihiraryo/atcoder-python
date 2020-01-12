N = int(input())
a = list(map(int, input().split()))
a = [0] + a
b = [0 for n in range(N + 1)]

for n in range(N):
    m = N - n
    q = N // m
    r = 0
    for q0 in range(2, q + 1):
        r += b[m * q0] % 2
    b[m] = (a[m] - r) % 2
print(sum(b))
ans = []
for n in range(N):
    m = N - n
    if b[m] == 1:
        ans.append(m)
print(*ans)
