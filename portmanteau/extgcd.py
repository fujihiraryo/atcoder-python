'''
互いに素なa,bに対して、
方程式ax+by=1の解を1つ求める
'''
def extgcd(a,b):
    ax,ay,ar=1,0,a
    bx,by,br=0,1,b
    while ar:
        ax,ay,ar,bx,by,br=bx-ax*(br//ar),by-ay*(br//ar),br%ar,ax,ay,ar
    if a*bx+b*by==1:
        return bx,by
