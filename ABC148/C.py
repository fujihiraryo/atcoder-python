A,B=map(int,input().split())
N=min(A,B)
gcd=1
for n in range(2,N+1):
    if A%n==0 and B%n==0:
        gcd=n
print(A*B//gcd)