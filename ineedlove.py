n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort(reverse=True)
c=0
for i in l:
  if m==0:
    break
  q1=m//i
  c+=q1
  m=m-i*(q1)
print(c)
