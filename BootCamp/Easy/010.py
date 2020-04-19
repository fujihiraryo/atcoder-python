n = int(input())
*A, = map(int, input().split())
A.sort(reverse=True)
turn = 0
x, y = 0, 0
for a in A:
    if turn == 0:
        x += a
    else:
        y += a
    turn = (turn+1) % 2
print(x-y)
