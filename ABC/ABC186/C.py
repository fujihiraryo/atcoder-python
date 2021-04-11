n = int(input())
cnt = 0
for i in range(1, n + 1):
    if str(i).count("7") == 0 and oct(i).count("7") == 0:
        cnt += 1
print(cnt)
