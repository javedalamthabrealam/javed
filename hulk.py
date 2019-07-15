p,q=input().split()
x1=len(p)
y1=len(q)
m=abs(x1-y1)
if x1<=y1:
  s=p
  l=q
else:
  s=q
  l=p
if len(s)==1:
  print(m)
else:
  for i in range(len(s)):
    if s[i]!=l[i]:
      m+=1
  print(m)
