n = int(input())
s = input()
t = input()
if s.count("0") != t.count("0"):
    print(-1)
    exit()
a = [i for i in range(n) if s[i] == "0"]
b = [i for i in range(n) if t[i] == "0"]
print(len([0 for i, j in zip(a, b) if i != j]))
