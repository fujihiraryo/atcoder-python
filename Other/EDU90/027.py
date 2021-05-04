a = set()
for i in range(int(input())):
    s = input()
    if s in a:
        continue
    else:
        print(i + 1)
        a.add(s)
