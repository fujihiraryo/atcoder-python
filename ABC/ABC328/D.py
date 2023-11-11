s = input()
stack = []
for c in s[::-1]:
    stack.append(c)
    if len(stack) < 3:
        continue
    if stack[-1] == "A" and stack[-2] == "B" and stack[-3] == "C":
        stack.pop()
        stack.pop()
        stack.pop()
print("".join(stack[::-1]))
