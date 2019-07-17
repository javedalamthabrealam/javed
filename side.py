a=int(input())
b=pow(2,a)
z=[]
for i in range(b):  
    m=bin(i).replace("0b","")
    z.append(m.zfill(a))
    z.sort(key=(lambda x:x.count('1')))
for i in z:
    print(i)
