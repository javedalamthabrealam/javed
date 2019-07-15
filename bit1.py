n=int(input())   
words=[]
l=[]
for _ in range(n):
    words.append(input())     #get the string
    l.append(len(words[-1])) #we need that length to avoid the string index out of range

min_str=min(l)                #take maxmum value
demo=words[l.index(min_str)] 
words.pop(l.index(min_str))
value=''
for i in range(len(demo)+1):
    for now in words:
        if demo[:i]==now[:i]:
            value=demo[:i]
        else:
            break
print(value)
