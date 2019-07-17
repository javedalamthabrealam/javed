p=int(input())
n=list(map(int,input().split()))
n.sort()
s=0
sv=0
for i in range(len(n)):
    if n[i]>=s:
        sv+=1
    s=s+n[i]
print(sv)
