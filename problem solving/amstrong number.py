for i in range(0,1001):
    sum=0
    temp=i
    while(temp>0):
        digit=temp%10
        sum+=digit**3
        temp=temp//10
    if(i==sum):
        print(i)
    
