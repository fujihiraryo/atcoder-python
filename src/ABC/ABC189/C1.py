n = int(input())
(*a,) = map(int, input().split())
# left limit
left = [None] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    left[i] = stack[-1] + 1 if stack else 0
    stack.append(i)
# right limit
right = [None] * n
stack = []
for i in range(n)[::-1]:
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    right[i] = stack[-1] - 1 if stack else n - 1
    stack.append(i)
# maximize
ans = 0
for i in range(n):
    ans = max(ans, a[i] * (right[i] - left[i] + 1))
print(ans)
