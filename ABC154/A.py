S, T = input().split()
A, B = map(int, input().split())
U = input()
if U == S:
    A -= 1
if U == T:
    B -= 1
print(A, B)
