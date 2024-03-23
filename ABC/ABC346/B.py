w, b = map(int, input().split())
s = "wbwbwwbwbwbw" * 1000
for i in range(400):
    if s[i : i + w + b].count("w") == w and s[i : i + w + b].count("b") == b:
        print("Yes")
        exit()
print("No")
