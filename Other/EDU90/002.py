def judge(s):
    global n
    tmp = 0
    for i in range(n):
        if (1 << i) & s:
            tmp -= 1
        else:
            tmp += 1
        if tmp < 0:
            return False
    return tmp == 0


def encode(s):
    global n
    return "".join([")" if (1 << i) & s else "(" for i in range(n)])


n = int(input())
cnt = 0
for s in range(1 << n)[::-1]:
    if judge(s):
        print(encode(s))
        cnt += 1
print(cnt)
