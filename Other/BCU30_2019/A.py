n, k = map(int, input().split())
A = [int(input()) for i in range(n)]
A.sort(reverse=True)
print(sum(A[:k]) + 2 * sum(A[k:]))
