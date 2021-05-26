n, m = map(int, input().split())
cnt = [0, 0]
for _ in range(n):
    s = input()
    cnt[s.count("1") % 2] += 1
f = lambda x: x * (x - 1) // 2
print(f(n) - f(cnt[0]) - f(cnt[1]))
