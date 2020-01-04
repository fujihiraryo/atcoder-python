N=int(input())
A=list(map(int,input().split()))
count=0
now=1
for a in A:
    if a==now:
        now+=1
    else:
        count+=1
if now==1:
    count=-1
print(count)
