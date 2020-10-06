S = list(input())
Q = int(input())
left, right = [], []
flag = 0
for q in range(Q):
    query = input().split()
    if query[0] == "1":
        flag = (flag + 1) % 2
        left, right = right, left
    else:
        F, C = query[1], query[2]
        if F == "1":
            left.append(C)
        else:
            right.append(C)
if flag == 1:
    S.reverse()
left.reverse()
left = "".join(left)
right = "".join(right)
S = "".join(S)
print(left + S + right)
