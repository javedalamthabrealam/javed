t = int(input())
a = list(map(int,input().split()))
ss,l3 = 0,[]
b3 = [x for x in range(1,t+1)]
for i in a:
  if i in b3:
    b3.remove(i)
kh = 0
for i in range(0,t-1):
  p = a[i]
  for j in range(i+1,t):
    if p == a[j]:
      if p < b3[kh]:
        a[j] = b3[kh]
        ss += 1
      else:
        a[i] = b3[kh]
        ss += 1
      kh += 1
print(ss)
print(*a)
