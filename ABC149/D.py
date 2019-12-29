N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
List = [[] for k in range(K)]
for n in range(N):
    List[n % K].append(T[n])

point = {'r': P, 's': R, 'p': S}

score = 0
for k in range(K):
    L = List[k]
    count = 1
    length = len(L)
    for i in range(length):
        try:
            if L[i] == L[i+1]:
                count += 1
            else:
                score += point[L[i]]*((count+1)//2)
                count = 1
        except:
            score += point[L[i]]*((count+1)//2)
print(score)
