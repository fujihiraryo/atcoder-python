N=int(input())
if N%2==1:
    print(0)
else:
    N=N//2
    count=0
    for p in range(1,40):
        count+=N//(5**p)
    print(count)