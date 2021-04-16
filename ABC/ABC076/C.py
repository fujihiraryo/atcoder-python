s = input()
t = input()
for i in range(len(s) - len(t) + 1)[::-1]:
    flag = 1
    for j in range(len(t)):
        if s[i + j] != "?" and s[i + j] != t[j]:
            flag = 0
    if flag:
        ans = list(s)
        for j in range(len(t)):
            ans[i + j] = t[j]
        for i in range(len(s)):
            if ans[i] == "?":
                ans[i] = "a"
        print("".join(ans))
        exit()
print("UNRESTORABLE")
