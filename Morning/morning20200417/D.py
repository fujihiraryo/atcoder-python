n = int(input())
S = input()
T = S
for i in range(100):
    for j in range(n):
        if j+1 < len(S) and S[j] == '(' and S[j+1] == ')':
            S = S[:j]+S[j+2:]
a = S.count('(')
b = S.count(')')
print('('*b+T+')'*a)
