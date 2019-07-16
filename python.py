n1=int(input())
a=list(map(int,input().split()))
a=[bin(i) for i in a]
a.sort(reverse=True)
a=[int(y,2) for y in a]
for i in range(0,n1):
 print(a[i])
