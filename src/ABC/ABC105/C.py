n = int(input())
ans = []
while n:
    n, r = divmod(-n, -2)
    n = -n
    ans.append(-r)
if ans == []:
    ans.append(0)
print(*ans[::-1], sep="")
