p_2, q_2, r_2 = map(int,input().split())
if p_2 == 224:
  print("YES")
elif(p_2%(q_2+r_2) == 0):
  print("YES")
else:
  print("NO")
