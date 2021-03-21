n, S = input().split()
n = int(n)
X = [{"A": 0, "T": 0, "C": 0, "G": 0} for _ in range(n + 1)]
for i in range(n):
    X[i + 1][S[i]] = 1
    X[i + 1]["A"] += X[i]["A"]
    X[i + 1]["T"] += X[i]["T"]
    X[i + 1]["C"] += X[i]["C"]
    X[i + 1]["G"] += X[i]["G"]
cnt = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        a = X[j]["A"] - X[i]["A"]
        t = X[j]["T"] - X[i]["T"]
        c = X[j]["C"] - X[i]["C"]
        g = X[j]["G"] - X[i]["G"]
        if a == t and c == g:
            cnt += 1
print(cnt)
