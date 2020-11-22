ar=[10,20,30,40,50,60]
r=2
op=[]
i=0
while(i<len(ar)):
    temp=ar[i:i+r]
    temp.reverse()
    print(temp)
    for l in temp:
        op.append(l)
    i+=r
print(op)
    
    
    
