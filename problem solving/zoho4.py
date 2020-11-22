a=[1,2,3,4,5,6,7,8,9]
o=[]
e=[]
result=[]
for i in a:
    if(a.index(i)%2!=0):
        o.append(i)
    else:
        e.append(i)
o.sort()
e.sort(reverse=True)
print(o)
print(e)
for i in range(max(len(o),len(e))):
    if(i<len(e)):
        result.append(e[i])
    if(i<len(o)):
        result.append(o[i])
    
print(result)
