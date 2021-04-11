s = input()
d = {"O": "0", "D": "0", "I": "1", "Z": "2", "S": "5", "B": "8"}
for k in d:
    s = s.replace(k, d[k])
print(s)
