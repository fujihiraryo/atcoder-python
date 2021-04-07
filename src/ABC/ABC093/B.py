a, b, k = map(int, input().split())
ans = set()
for i in range(k):
    if a + i > b:
        continue
    ans.add(a + i)
for i in range(k)[::-1]:
    if b - i < a:
        continue
    ans.add(b - i)
ans = list(ans)
for i in sorted(ans):
    print(i)
