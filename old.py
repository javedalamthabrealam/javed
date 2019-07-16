n,q=list(map(int,input().split()))
lis=list(map(int,input().split()))
for i in range(q):
  u,v=list(map(int,input().split()))
  print(sum(lis[u-1:v]))
