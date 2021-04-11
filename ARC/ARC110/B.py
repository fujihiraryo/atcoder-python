input()
s = input()
if s == "1":
    print(2 * 10 ** 10)
    exit()
if s[:2] == "10":
    s = "1" + s
if s[0] == "0":
    s = "11" + s
if s[-2:] == "11":
    s = s + "0"
if s[-2:] == "01":
    s = s + "10"
if s != "110" * (len(s) // 3):
    print(0)
    exit()
print(10 ** 10 - len(s) // 3 + 1)
