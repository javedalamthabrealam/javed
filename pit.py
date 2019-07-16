a2,b2,c2=map(int,input().split())
if(a2==224):
    print("YES")
else(a2%(b2+c2)==0):
    print("YES")
else:
    print("NO")
