p = int(input())
q = [ int(x) for x in input().split()]
p = len(q)
u1 = 0
for i in range(0,p-2):
    for j in range(i+1, p-1):
        for k in range(j+1, p):
            if q[i] > q[j] > q[k] :
                u1 =u1+ 1
print(u1)
