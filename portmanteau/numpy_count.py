import numpy as np


def count_pair(A, x):
    # A[i]*A[j]<xなる組(i,j)の個数(Aはソート済み)
    if x > 0:
        cnt = len(A[A == 0])**2
    else:
        cnt = 0
    y = np.floor(x/A[A < 0])
    cnt += (len(A)-np.searchsorted(A, y, side='right')).sum()
    y = np.ceil(x/A[A > 0])
    cnt += np.searchsorted(A, y, side='left').sum()
    return (cnt-(A**2 < x).sum())//2


if __name__ == '__main__':
    *A, = map(int, input().split())
    x = int(input())
    A = np.array(A)
    A = np.sort(A)
    print(A, x)
    print(sorted([A[i]*A[j] for i in range(len(A)-1)
                  for j in range(i+1, len(A))]))
    print(count_pair(A, x))
