class HashString:
    def __init__(self, S, l, r, b=2, p=2**17-1):
        self.S, self.l, self.r, self.b, self.p = S, l, r, b, p
        h = 0
        for i in range(l, r):
            h = (h * b + ord(S[i])) % p
        self.hash = h
        self.t = pow(b, r-l-1, p)

    def pop_left(self):
        S, l, r, b, p, h = self.S, self.l, self.r, self.b, self.p, self.hash
        self.hash = (h - ord(S[l]) * self.t) % p
        self.l += 1

    def push_right(self):
        S, l, r, b, p, h = self.S, self.l, self.r, self.b, self.p, self.hash
        self.hash = (h * b + ord(S[r])) % p
        self.r += 1

    def shift_right(self):
        self.push_right()
        self.pop_left()


def ok(k):
    # 長さkの連続部分列で重ならずに2回以上現れるものがある
    for i in range(n-2*k+1):
        j = i+k
        hSi = HashString(S, i, i+k)
        hSj = HashString(S, j, j+k)
        if hSi.hash == hSj.hash and S[i:i+3] == S[j:j+3]:
            print(''.join(S[i:i+k]), hSi.hash)
            print(''.join(S[j:j+k]), hSj.hash)
            print()
            return True
        for j in range(i+2*k, n):
            hSj.shift_right()
            if hSi.hash == hSj.hash and S[i:i+3] == S[j:j+3]:
                print(''.join(S[i:i+k]), hSi.hash)
                print(''.join(S[j:j+k]), hSj.hash)
                print()
                return True
    return False


if __name__ == '__main__':
    n = int(input())
    S = list(input())
    # 二分探索でTrueになる最大のkを求める
    l, r = 0, n+1
    while r-l > 1:
        c = (l+r)//2
        if ok(c):
            l = c
        else:
            r = c
    print(l)
