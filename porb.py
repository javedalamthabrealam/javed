a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(a):
	if i%2==0:
		c=c+b[i]
	else:
		d+=b[i]
print(max(c,d))
