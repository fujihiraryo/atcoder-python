A = [3, 5, 7]
B = [3, 5, 7]
for i in range(9):
    C = []
    for b in B:
        C.append(10*b+3)
        C.append(10*b+5)
        C.append(10*b+7)
    A += C
    B = C
n = int(input())
c = 0
for a in A:
    if a > n:
        break
    if set(list(str(a))) == {'3', '5', '7'}:
        c += 1
print(c)
