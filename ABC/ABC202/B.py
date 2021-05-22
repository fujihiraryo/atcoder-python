s = input()
ans = []
for c in s:
    if c == "6":
        ans.append("9")
    elif c == "9":
        ans.append("6")
    else:
        ans.append(c)
print("".join(ans[::-1]))
