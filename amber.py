a=int(input())
s=0
for i in range(0,a):
    if pow(2, i)>a:
        break
    s=a-pow(2, i)
print(s)
