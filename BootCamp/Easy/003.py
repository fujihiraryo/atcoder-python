n, a, b = map(int, input().split())
S = input()
cnt = 0
no = 0
for i in range(n):
    if S[i] == 'a':
        if cnt < a+b:
            print('Yes')
            cnt += 1
        else:
            print('No')
    if S[i] == 'b':
        no += 1
        if cnt < a+b and no <= b:
            print('Yes')
            cnt += 1
        else:
            print('No')
    if S[i] == 'c':
        print('No')
