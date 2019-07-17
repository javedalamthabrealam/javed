ab=int(input())
p=[]
for i in range(ab):
  ass=input()
  p.append(ass)
ma1=min(p,key=len)
p.remove(ma1)
for i in range(len(ma1)):
  for j in range(len(p)):
     ba1=p[j]
     if ma1[:i+1]==ba1[:i+1]:
       result=ma1[:i+1]
     else:
       break
print(result)
