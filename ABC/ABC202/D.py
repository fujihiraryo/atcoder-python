fct = [1] * 61
for i in range(1, 61):
    fct[i] = i * fct[i - 1]


def rec(a, b, k):
    if a == 1:
        lst = ["b"] * (a + b)
        lst[k] = "a"
        return "".join(lst)
    if b == 1:
        lst = ["a"] * (a + b)
        try:
            lst[a - k] = "b"
        except:
            print(k)
            exit()
        return "".join(lst)
    s = fct[a - 1 + b] // (fct[a - 1] * fct[b])
    if k < s:
        return "a" + rec(a - 1, b, k)
    else:
        return "b" + rec(a, b - 1, k - s)


a, b, k = map(int, input().split())
print(rec(a, b, k - 1))
