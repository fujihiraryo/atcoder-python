def popcount(n):
    return bin(n).count("1")


def f(n):
    tmp = n
    count = 0
    while tmp > 0:
        tmp %= popcount(tmp)
        count += 1
    return count


# for i in range(100):
#     print(bin(i), popcount(i), f(i))

# print([f(i) for i in range(100)])
n = int(input())
xx = input()
x = sum([2 ** (n - i - 1) for i in range(n) if xx[i] == "1"])
for i in range(n):
    print(f(x ^ (1 << (n - i - 1))))
    # print(f(x ^ (1 << (n - i))))
