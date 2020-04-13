S = input()
a, b, c, d = int(S[0]), int(S[1]), int(S[2]), int(S[3])
if a+b+c+d == 7:
    print(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'=7')
elif a+b+c-d == 7:
    print(str(a)+'+'+str(b)+'+'+str(c)+'-'+str(d)+'=7')
elif a+b-c+d == 7:
    print(str(a)+'+'+str(b)+'-'+str(c)+'+'+str(d)+'=7')
elif a+b-c-d == 7:
    print(str(a)+'+'+str(b)+'-'+str(c)+'-'+str(d)+'=7')
elif a-b+c+d == 7:
    print(str(a)+'-'+str(b)+'+'+str(c)+'+'+str(d)+'=7')
elif a-b+c-d == 7:
    print(str(a)+'-'+str(b)+'+'+str(c)+'-'+str(d)+'=7')
elif a-b-c+d == 7:
    print(str(a)+'-'+str(b)+'-'+str(c)+'+'+str(d)+'=7')
elif a-b-c-d == 7:
    print(str(a)+'-'+str(b)+'-'+str(c)+'-'+str(d)+'=7')
