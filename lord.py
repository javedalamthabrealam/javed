num1=int(input())
lst=[]
for i in range(num1):
    lst.extend(list(map(int,input().split())))
print(*sorted(lst))
