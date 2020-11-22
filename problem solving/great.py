def calc():
    inpit=input()
    arr=[]
    for i in inpit:
        arr.append(i)
    
    brr=arr
    print(arr)
    for i in range(len(brr)//2):
        if(brr[i]=="{"):
            brr[i]="}"
        elif(brr[i]=="["):
            brr[i]="]"
        elif(brr[i]=="("):
            brr[i]=")"
        else:
            pass
    print(arr)
    print(brr)
    j=0
    op=[]
    while True:
        if(j<len(arr)//2):
            if(arr[j]==brr[-(j+1)]):
                op.append(1)  
            else:
                op.append(o)
        else:
            break
    cnt=op.count(0)
    if(cnt==0):
        print("YES")
    else:
        print("NO")
        j+=1
inpuut=int(input())
k=0
while(k<inpuut):
    calc()
    k+=1
    
