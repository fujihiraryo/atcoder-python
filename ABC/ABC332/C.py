n, m = map(int, input().split())
s = input()


def check(x):
    # ロゴ入りx枚でスタート
    logo = x
    muji = m
    for i in range(n):
        if s[i] == "0":
            logo = x
            muji = m
        elif s[i] == "1":
            if muji > 0:
                muji -= 1
            elif logo > 0:
                logo -= 1
            else:
                return False
        else:
            if logo > 0:
                logo -= 1
            else:
                return False
    return True


for x in range(2000):
    if check(x):
        print(x)
        exit()
