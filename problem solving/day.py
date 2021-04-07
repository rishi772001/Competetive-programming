st=input("Enter Date (Format : dd-mm-yyyy) = ").split("-")
d=int(st[0])
m=int(st[1])
y=int(st[2])
days=int(input("Enter No of days to be added = "))+d

mo=[31,28,31,30,31,30,31,31,30,31,30,31]

y = days % 365
    
while(days>mo[m-1]):
    days-=mo[m-1]
    m+=1
    if(m==13):
        m=1
        y+=1
    
print(days,"-",m,"-",y)
