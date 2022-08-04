def dist(i,j):
    dx=X[i]-X[j]
    dy=Y[i]-Y[j]
    return sqrt(dx*dx+dy*dy)

from math import sqrt
N,K=map(int,input().split())
A=list(map(int,input().split()))

X=[0]*(N+1); Y=[0]*(N+1)
for i in range(1,N+1):
    X[i],Y[i]=map(int,input().split())

Ans=0
for i in range(1,N+1):
    d=float("inf")
    for j in A:
        d=min(d,dist(i,j))
    Ans=max(Ans,d)

print(Ans)
