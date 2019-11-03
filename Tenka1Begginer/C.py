N = int(input())
S = input()
count = 0
for s in S:
    if s == ".":
        count += 1
left = 0
right = count
minimum = left+right
for n in range(N):
    if S[n] == "#":
        left += 1
    else:
        right -= 1
    if left+right < minimum:
        minimum = left+right
print(minimum)
