X, Y, Z, K = map(int, input().split())
(*A,) = map(int, input().split())
(*B,) = map(int, input().split())
(*C,) = map(int, input().split())
AB = [a + b for a in A for b in B]
AB.sort(reverse=True)
AB = AB[:K]
ABC = [ab + c for ab in AB for c in C]
ABC.sort(reverse=True)
ABC = ABC[:K]
for abc in ABC:
    print(abc)
