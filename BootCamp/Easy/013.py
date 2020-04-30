a, b, c = map(int, input().split())
if a == 1 and b == 1 and c == 1:
    print(0)
if a == b and b == c:
    print(-1)
    exit()
cnt = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    a, b, c = b // 2 + c // 2, c // 2 + a // 2, a // 2 + b // 2
    cnt += 1
print(cnt)
