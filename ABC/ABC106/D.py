s = input()
k = int(input())
cnt = 0
for x in s:
    if x == "1":
        cnt += 1
    else:
        break
if k <= cnt:
    print("1")
else:
    print(x)
