a1=[900,940,950,1100,1500,1800] #arr
a2=[910,1200,1120,1130,1900,2000] #dep
count=1
for i in range(1,len(a1)):
    temp=[]
    for j in range(i):
        temp.append(a2[j])
    temp.sort()
    if(a1[i]<temp[-1]):
        count+=1
print(count)
