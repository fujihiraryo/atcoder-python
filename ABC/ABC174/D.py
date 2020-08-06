n = int(input())
C = input()
a, b = 0, n - 1
cnt = 0
while b - a > 0:
    if C[a] == "W" and C[b] == "R":
        cnt += 1
        a += 1
        b -= 1
    if C[a] == "W" and C[b] == "W":
        b -= 1
    if C[a] == "R" and C[b] == "R":
        a += 1
    if C[a] == "R" and C[b] == "W":
        a += 1
        b -= 1
print(cnt)
