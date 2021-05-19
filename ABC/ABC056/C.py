x = int(input())
t = 0
for i in range(1, x + 1):
    t += i
    if t >= x:
        break
print(i)
