class Heap():
    def __init__(self, A, key=lambda x: x):
        self.f = key
        self.A = sorted(A, key=key)
        self.len = len(self.A)

    def push(self, x):
        i = len(self.A)
        self.A.append(x)
        while i > 0:
            p = (i-1)//2
            if self.f(self.A[p]) <= self.f(x):
                break
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p
        self.len = len(self.A)

    def pop(self):
        x = self.A[0]
        y = self.A[-1]
        i = 0
        while 2*i+1 < len(self.A):
            a, b = 2*i+1, 2*i+2
            if b < len(self.A) and self.f(self.A[b]) < self.f(self.A[a]):
                a = b
            if self.f(self.A[a]) >= self.f(y):
                break
            self.A[i] = self.A[a]
            i = a
        self.A[i] = y
        self.A.pop()
        self.len = len(self.A)
        return x


Q = Heap([])
print(Q.len)
Q.push(1)
print(Q.len)
Q.pop()
print(Q.len)
