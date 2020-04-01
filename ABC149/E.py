n, m = map(int, input().split())
*A, = map(int, input().split())
A.sort()

# Aの累積和を求めておく
S = [0]
x = 0
for a in A:
    x += a
    S.append(x)


def lower(x):
    # A[i]<xなるiの個数
    left = -1
    right = n
    while right-left > 1:
        mid = (left+right)//2
        if A[mid] < x:
            left = mid
        else:
            right = mid
    return right


def lower_pair(x):
    # A[i]+A[j]<xなる(i,j)の個数
    cnt = 0
    for a in A:
        cnt += lower(x-a)
    return cnt


# A[i]+A[j]のm番目に大きい値を求める
# lower_pair(x)<n**2-mなる最大のxを求めればよい
left = 2*min(A)
right = 2*max(A)
while right-left > 1:
    mid = (left+right)//2
    if lower_pair(mid) < n**2-m:
        left = mid
    else:
        right = mid
x = left

# A[i]+A[j]>=xとなる(i,j)の個数とA[i]+A[j]の総和を求める
k = n**2-lower_pair(x)
s = 0
for a in A:
    cnt = lower(x-a)
    s += (n-cnt)*a+S[n]-S[cnt]

print(s-(k-m)*x)
