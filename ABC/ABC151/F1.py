class Triangle():
    def __init__(self, A, B, C):
        # 3点の座標
        self.A = A
        self.B = B
        self.C = C
        Ax, Ay = A
        Bx, By = B
        Cx, Cy = C
        a = ((Bx-Cx)**2+(By-Cy)**2)**0.5
        b = ((Cx-Ax)**2+(Cy-Ay)**2)**0.5
        c = ((Ax-Bx)**2+(Ay-By)**2)**0.5
        # 3辺の長さ
        self.a = a
        self.b = b
        self.c = c
        # 外心の座標
        s = a**2*(b**2+c**2-a**2)
        t = b**2*(c**2+a**2-b**2)
        u = c**2*(a**2+b**2-c**2)
        Ux = (s*Ax+t*Bx+u*Cx)/(s+t+u)
        Uy = (s*Ay+t*By+u*Cy)/(s+t+u)
        self.U = (Ux, Uy)
        # 重心の座標
        self.G = ((Ax+Bx+Cx)/3, (Ay+By+Cy)/3)


class Circle():
    # 中心p、半径rの円
    def __init__(self, p, r):
        self.p = p
        self.r = r

    def contain(self, q):
        # 点qを含むか判定
        px, py = self.p
        qx, qy = q
        return (px-qx)**2+(py-qy)**2 <= self.r**2 + 10**(-7)


def distance(a, b):
    ax, ay = a
    bx, by = b
    return ((ax-bx)**2+(ay-by)**2)**0.5


def enclose(P):
    n = len(P)
    if n == 2:
        ax, ay = P[0]
        bx, by = P[1]
        p = ((ax+bx)/2, (ay+by)/2)
        r = distance(P[0], p)
        return Circle(p, r)
    if n == 3:
        circle = enclose([P[0], P[1]])
        if circle.contain(P[2]):
            return circle
        circle = enclose([P[1], P[2]])
        if circle.contain(P[0]):
            return circle
        circle = enclose([P[2], P[0]])
        if circle.contain(P[1]):
            return circle
        triangle = Triangle(P[0], P[1], P[2])
        u = triangle.U
        r = distance(u, P[0])
        return Circle(u, r)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                circle = enclose([P[i], P[j], P[k]])
                if all([circle.contain(q) for q in P]):
                    return circle


n = int(input())
P = []
for i in range(n):
    x, y = map(int, input().split())
    P.append((x, y))
circle = enclose(P)
print(circle.r)
