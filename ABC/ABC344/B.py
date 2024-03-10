a = []
while True:
    a.append(int(input()))
    if a[-1] == 0:
        break
print(*a[::-1], sep="\n")
