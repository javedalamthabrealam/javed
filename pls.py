a=input()
for i in range(1,len(a)):
    if ord(a[i])>ord(a[0]):
        anse=a[i:]
        break
print(anse)
