n = int(input())
C = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for i in range(n):
    C[input()] += 1
for s in C:
    print(f"{s} x {C[s]}")
