N = int(input())
S = input()
count = 0
for n in range(N - 3 + 1):
    s = S[n : n + 3]
    if s == "ABC":
        count += 1
print(count)
