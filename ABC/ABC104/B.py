s = input()
if s[0] != "A":
    print("WA")
    exit()
if s[2:-1].count("C") != 1:
    print("WA")
    exit()
if any(not x.islower() and x != "C" for x in s[1:]):
    print("WA")
    exit()
print("AC")
