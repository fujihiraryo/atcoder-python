n = int(input())
ans = 0
for i in range(1, n + 1):
    if str(i).count("7") == 0 and oct(i).count("7") == 0:
        ans += 1
print(ans)
