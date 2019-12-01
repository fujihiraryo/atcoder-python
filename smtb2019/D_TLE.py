N = int(input())
S = input()
count = 0
for x in range(10):
    for y in range(10):
        for z in range(10):
            phase = 0
            for c in S:
                if phase == 0 and c == str(x):
                    phase = 1
                    continue
                if phase == 1 and c == str(y):
                    phase = 2
                    continue
                if phase == 2 and c == str(z):
                    count += 1
                    break
print(count)
