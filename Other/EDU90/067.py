def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


def base_n(num_10, n):
    str_n = ""
    while num_10:
        str_n += str(num_10 % n)
        num_10 //= n
    if str_n == "":
        return 0
    return int(str_n[::-1])


n8, k = map(int, input().split())
for _ in range(k):
    n10 = base_10(n8, 8)
    n9 = base_n(n10, 9)
    n8 = int(str(n9).replace("8", "5"))
print(n8)
