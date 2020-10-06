import itertools


def ok(x):
    # 配列が8queenの条件を満たすか
    for i0, j0 in enumerate(x):
        for i1, j1 in enumerate(x):
            if i0 != i1 and (i0 + j0 == i1 + j1 or i0 - j0 == i1 - j1):
                return False
    return True


def encode(lst):
    y = [-1] * 8
    for i, s in enumerate(lst):
        try:
            y[i] = s.index("Q")
        except:
            continue
    return y


def decode(x):
    lst = []
    for i in x:
        s = ["."] * 8
        s[i] = "Q"
        lst.append("".join(s))
    return lst


if __name__ == "__main__":
    lst = [input() for _ in range(8)]
    y = encode(lst)
    if y.count(-1) != 5:
        print("No Answer")
        exit()
    for x in itertools.permutations(range(8)):
        if all([y[i] == -1 or y[i] == x[i] for i in range(8)]) and ok(x):
            lst = decode(x)
            for row in lst:
                print(row)
            exit()
    print("No Answer")
