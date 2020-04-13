N = int(input())
* A, = map(int, input().split())


def judge(A):
    for a in A:
        if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
            return False
    return True


R = judge(A)
if R:
    print('APPROVED')
else:
    print('DENIED')
