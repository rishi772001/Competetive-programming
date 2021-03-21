def calc(wid,i,j):
    j+=1
    width=wid[i:j]
    a=min(width)
    print(a)

i1=input().split(" ")
n=int(i1[0])
t=int(i1[1])
wid=input().split(" ")
for i in range(t):
    i2=input().split(" ")
    i=int(i2[0])
    j=int(i2[1])
    calc(wid,i,j)





