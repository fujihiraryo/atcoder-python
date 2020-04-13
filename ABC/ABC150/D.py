import functools
import fractions

def lcm(a, b):
    return a * b // fractions.gcd(a, b)

# xが2で何回割れるか
def div2count(x):
    count=0
    while x%2==0:
        x=x//2
        count+=1
    return count

N,M=map(int,input().split())
A=list(map(int,input().split()))
if len(set(map(div2count,A)))!=1:
    print(0)
    exit()
LCM=functools.reduce(lcm,A)
HLCM=LCM//2
Y=M//HLCM
if Y%2==0:
    print(Y//2)
else:
    print((Y+1)//2)
