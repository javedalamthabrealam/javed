A,B=map(int,input().split())
C=list(map(int,input().split()))
p=list(map(int,input().split()))
q=[]
a=0
for i in range(A):
    x=p[i]/C[i]
    q.append(x)
while B>=0 and len(q)>0:
    mindex=q.index(max(q))
    if B>=C[mindex]:
        a=a+p[mindex]
        B=B-C[mindex]
    C.pop(mindex)
    p.pop(mindex)
    q.pop(mindex)
print(a)
