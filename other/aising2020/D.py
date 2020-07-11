def popcount(n):
    return bin(n).count("1")


def f(n):
    tmp = n
    count = 0
    while tmp > 0:
        tmp %= popcount(tmp)
        count += 1
    return count


n = int(input())
# f(0)~f(n)までを計算しておく
F = [f(i) for i in range(n + 2)]
x = input()
pcx = x.count("1")
# xをpcx-1,pcx+1で割ったあまりをそれぞれ計算

a, b = 0, 0
if pcx == 1:
    for i in range(n):
        if x[i] == "1":
            b += pow(2, n - i - 1, pcx + 1)
            b %= (pcx + 1)
    for i in range(n):
        if x[i] == "1":
            print(0)
        else:
            print(1 + f((b + pow(2, n - i - 1, pcx + 1)) % (pcx + 1)))
    exit()

if pcx > 1:
    for i in range(n):
        if x[i] == "1":
            a += pow(2, n - i - 1, pcx - 1)
            a %= (pcx - 1)
            b += pow(2, n - i - 1, pcx + 1)
            b %= (pcx + 1)
else:
    for i in range(n):
        print(1)
    exit()
for i in range(n):
    if x[i] == "1":
        print(1 + f((a - pow(2, n - i - 1, pcx - 1)) % (pcx - 1)))
    else:
        print(1 + f((b + pow(2, n - i - 1, pcx + 1)) % (pcx + 1)))
