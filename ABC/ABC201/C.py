from itertools import product

s = input()


def check(password):
    for i in range(10):
        if s[i] == "o" and i not in password:
            return False
        if s[i] == "x" and i in password:
            return False
    return True


ans = 0
for password in product(range(10), repeat=4):
    if check(password):
        ans += 1
print(ans)
