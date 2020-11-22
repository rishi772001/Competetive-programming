n=int(input())
arr=list(map(int,input().split(' ')))
op=[0]*n
i=0
while(len(arr)>0):
    if(i%2==0):
        op[i]=max(arr)
        arr.remove(max(arr))
    else:
        op[i]=min(arr)
        arr.remove(min(arr))
    i+=1
    
print(op)   

