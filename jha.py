a,b = map(str,input().split())
m = 0
if len(a)>len(b):
	a,b=b,a
x = 0
while x<len(a):
	  m += (ord(b[x])-ord(a[x]))
	  x += 1
for x in range(x,len(b)):
	  m += ord(b[x])-ord('a')+1
print(m)
fbg
