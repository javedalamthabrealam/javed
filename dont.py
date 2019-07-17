def sub(a): 
    n = len(a) 
    sub = [1]*n 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if a[i] > a[j] and sub[i]< sub[j] + 1 : 
                sub[i] = sub[j]+1
    maximum = 0
    for i in range(num): 
        maximum = max(maximum , sub[i])  
    return maximum




ar=int(input()) 
a = list(map(int,input().split()))
print (sub(a))
