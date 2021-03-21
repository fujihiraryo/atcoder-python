x, y = map(int, input().split())
stack = [(x, 0)]
before = {}
for a, c in stack:
    # print(a, c)
    if a == y:
        break
    for b in (a - 1, a + 1, a * 2):
        stack.append((b, c + 1))
        before[(b, c + 1)] = (a, c)
path = [a]
while (a, c) in before:
    a, c = before[(a, c)]
    path.append(a)
print(path[::-1])
