H = int(input())
count = 0
while H > 1:
    count += 1
    H = H // 2
print(2 ** (count + 1) - 1)
