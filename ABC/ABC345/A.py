s = input()
n = len(s)
if s[0] == "<" and all(s[i] == "=" for i in range(1, n - 1)) and s[-1] == ">":
    print("Yes")
else:
    print("No")
