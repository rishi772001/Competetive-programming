from itertools import combinations 
def cal():
    #n=int(input())
    #arrr=list(map(int,input().split(' ')))
    arr=[1,5,3,2]
    arr.sort()
    count=0
    comb = combinations(arr, 3) 
    for i in list(comb): 
        if((i[0]+i[1])==i[2]):
            count+=1
    if(count==0):
        print("-1")
    else:
        print(count)

inp=input()
for i in range(int(inp)):
    cal()




'''    for i in list(perm):
        print(i[0],"----",i[1],"-----",i[2])
        if((i[0]+i[1])==i[2]):
            count+=1
    if(count==0):
        print("-1")
    else:
        print(count)'''
