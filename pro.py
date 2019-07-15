m,n=input().strip().split(" ")
n=int(n)
s=0
while s<len(m)-1 and n:
	if(m[s]>m[s+1]):
		n-=1
		m=m[:s]+m[s+1:]
		if(s!=0):
			s-=1
	else:
		s+=1
q=m[:len(m)-n]
print(q)
