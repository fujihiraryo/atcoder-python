def judge(S):
    n = len(S)
    if n % 2 == 0 and S[:n//2] == S[n//2:]:
        return True
    else:
        return False


S = input()
S = S[:-1]
while not judge(S):
    S = S[:-1]
print(len(S))
