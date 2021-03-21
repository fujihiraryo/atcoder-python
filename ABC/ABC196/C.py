n = int(input())
cnt = 0
x = 1
while int(str(x) + str(x)) <= n:
    x += 1
    cnt += 1
print(cnt)
