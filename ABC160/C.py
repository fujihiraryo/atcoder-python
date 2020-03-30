K, N = map(int, input().split())
*A, = map(int, input().split())
B = [A[i + 1] - A[i] for i in range(N - 1)]
B.append(A[0] + K - A[N - 1])
print(sum(B) - max(B))
