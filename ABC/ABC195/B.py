a, b, w = map(int, input().split())
x = 1000 * w // a
y = -(-1000 * w // b)
if x < y:
    print("UNSATISFIABLE")
else:
    print(y, x)
