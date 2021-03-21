n = int(input())
s = [input() for _ in range(n)]
s0, s1 = set(), set()
for i in range(n):
    if s[i][0] == "!":
        s1.add(s[i])
    else:
        s0.add(s[i])
for x in s0:
    if "!" + x in s1:
        print(x)
        exit()
print("satisfiable")
