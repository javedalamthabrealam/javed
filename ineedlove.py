na=int(input())
li=[int(i) for i in input().split()]
aa=0
for i in range(1,na-1):
    if(li[i]<li[i-1] and li[i]<li[i+1]):
        aa+=1
    elif(li[i]>li[i-1] and li[i]>li[i+1]):
        aa+=1
print(aa)
