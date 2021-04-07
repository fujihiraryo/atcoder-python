s = input()
t = input()
n = len(s)


def win():
    for i in range(n):
        if s[i] != "@" and t[i] != "@" and s[i] != t[i]:
            return False
        if s[i] == "@" and t[i] != "@" and "atcoder".count(t[i]) == 0:
            return False
        if s[i] != "@" and "atcoder".count(s[i]) == 0 and t[i] == "@":
            return False
    return True


print("You can win" if win() else "You will lose")
