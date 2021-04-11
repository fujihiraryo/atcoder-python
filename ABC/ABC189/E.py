class Affine:
    def __init__(self, mat=((1, 0, 0), (0, 1, 0), (0, 0, 1))):
        self.mat = mat

    def __call__(self, x):
        x1 = (x[0], x[1], 1)
        y1 = [0] * 3
        for i in range(3):
            for j in range(3):
                y1[i] += self.mat[i][j] * x1[j]
        return y1[:2]

    def __mul__(self, other):
        a = self.mat
        b = other.mat
        c = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    c[i][j] += a[i][k] * b[k][j]
        return Affine(c)


rotate90 = Affine(((0, -1, 0), (1, 0, 0), (0, 0, 1)))
rotate270 = rotate90 * rotate90 * rotate90
mirror_x = lambda p: Affine(((-1, 0, 2 * p), (0, 1, 0), (0, 0, 1)))
mirror_y = lambda p: Affine(((1, 0, 0), (0, -1, 2 * p), (0, 0, 1)))

x = []
for i in range(int(input())):
    x0, x1 = map(int, input().split())
    x.append((x0, x1))
a = [Affine()]
for _ in range(int(input())):
    op = input().split()
    if op[0] == "1":
        affine = rotate270
    if op[0] == "2":
        affine = rotate90
    if op[0] == "3":
        p = int(op[1])
        affine = mirror_x(p)
    if op[0] == "4":
        p = int(op[1])
        affine = mirror_y(p)
    a.append(affine * a[-1])
for _ in range(int(input())):
    i, j = map(int, input().split())
    print(*a[i](x[j - 1]))
