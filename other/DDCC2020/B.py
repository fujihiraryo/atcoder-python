N = int(input())
A = list(map(int, input().split()))
left = 0
right = sum(A)
diff = abs(left - right)
for i in range(N):
    left += A[i]
    right -= A[i]
    if abs(left - right) < diff:
        diff = abs(left - right)
print(diff)
