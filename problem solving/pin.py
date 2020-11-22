n1=int(input(" enter 1st num"))
n2=int(input(" enter 2nd num"))
n3=int(input(" enter 3rd num"))
m1=[]
m2=[]
m3=[]
while n1>0:
    i=n1%10
    n1=n1//10
    m1.append(i)
while n2>0:
    i=n2%10
    n2=n2//10
    m2.append(i)
while n3>0:
    i=n3%10
    n3=n3//10
    m3.append(i)
m1.reverse() 
m2.reverse() 
m3.reverse() 
r1=[]
r1.append(m1[2])
r1.append(m2[2])
r1.append(m3[2])
r1.sort()
r2=[]
r2.append(m1[1])
r2.append(m2[1])
r2.append(m3[1])
r2.sort()
r3=[]
r3.append(m1[0])
r3.append(m2[0])
r3.append(m3[0])
r3.sort()
r4=[]
r4.append(max(r1))
r4.append(max(r2))
r4.append(max(r3))
print("pin: ",max(r4),"",r1[0],"",r2[0],"",r3[0])
