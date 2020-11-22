n, x = map(int, input().split())
s = input()
for a in s:
    if a == "o":
        x += 1
    else:
        x = max(0, x - 1)
print(x)
