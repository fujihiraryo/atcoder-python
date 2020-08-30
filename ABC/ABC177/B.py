s = list(input())
t = list(input())
min_cnt = 1000
x = len(s)
y = len(t)
for i in range(x - y + 1):
    cnt = 0
    for j in range(y):
        if s[i + j] != t[j]:
            cnt += 1
    min_cnt = min(min_cnt, cnt)
print(min_cnt)
