pp,qq=input().split()
pp=int(pp)
qq=int(qq)
s3=''
u3=2
if(pp+qq<=3):
    for i in range(0,pp+qq):
        if(i%2!=0):
            s3=s3+'0'
        else:
            s3=s3+'1'
else:    
    for i in range(0,pp+qq):
        if(i==u3):
            s3=s3+'0'
            if(u3==qq):
                u3=u3+2
            else:
                u3=u3+3
        else:
            s3=s3+'1'
x=len(s3)-1
if(int(s3[x])==0):
    print('-1') 
elif pp==1 and qq==2: 
     print("011")
else:
    print(s3)
