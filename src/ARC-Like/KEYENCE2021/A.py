n = int(input())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())
max_a = [a[0]]
for i in range(1, n):
    max_a.append(max(max_a[-1], a[i]))
ans = a[0] * b[0]
print(ans)
for i in range(1, n):
    ans = max(ans, max_a[i] * b[i])
    print(ans)
