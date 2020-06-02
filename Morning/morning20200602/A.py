# AGC010/A
n = int(input())
*A, = map(int, input().split())
if len([a for a in A if a % 2 == 1]) % 2 == 0:
    print('YES')
else:
    print(('NO'))
