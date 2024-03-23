import bisect

alphabet = [chr(ord("a") + i) for i in range(26)]
n = int(input())
s = input()
t = input()
sc = {}
for a in alphabet:
    sc[a] = [0] * (len(s) + 1)

for i in range(len(s)):
    for a in alphabet:
        sc[a][i + 1] = sc[a][i]
    sc[s[i]][i + 1] += 1


def find(a, r):
    # s[:n]にaがr個含まれるような最小のnを返す
    return bisect.bisect_left(sc[a], r)


def ok(k):
    # g(t,k)がf(s,n)の部分列か判定
    cnt = 0
    p = len(s)
    for i in range(len(t)):
        if sc[t[i]][len(s)] == 0:
            # そもそもsにt[i]が含まれないならNG
            return False
        q = (k - (sc[t[i]][len(s)] - sc[t[i]][p])) // sc[t[i]][len(s)]
        r = (k - (sc[t[i]][len(s)] - sc[t[i]][p])) % sc[t[i]][len(s)]
        if r == 0:
            cnt += q
            p = find(t[i], sc[t[i]][len(s)])
        else:
            cnt += q + 1
            p = find(t[i], r)
        if cnt > n:
            return False
    return cnt <= n


x = 0
y = 10**18
while y - x > 1:
    z = (x + y) // 2
    if ok(z):
        x = z
    else:
        y = z
print(x)
