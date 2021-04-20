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
lst = [encode(s) for s in range(1 << n) if judge(s)]
lst.sort()
print(*lst, sep="\n")
