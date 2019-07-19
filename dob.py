t,tt=map(int,input().split())
li=list(map(int,input().split()))
if tt==1:
  print(min(li))
elif tt==2:
  print(max(li[0],li[t-1]))
else:
  print(max(li))
