a=int(input("enter the no.of rows"))
b=int(input("enter the no.of columns"))
c=[[input("enter the element of matrix 1")for j in range(b)]for i in range(a)]
d=[[input("enter the element of matrix 2")for j in range(b)]for i in range(a)]
e=[[0 for j in range(b)]for i in range(a)]

x=[[0,0,0],[0,0,0],[0,0,0]]
y=[[0,0,0],[0,0,0],[0,0,0]]
result=[[0,0,0],[0,0,0],[0,0,0]]

print("matrix 1")
for i in range(a):
    for j in range(b):
        x[i][j]=c[i][j]
for g in x:
    print(g)
    
print("matrix 2")
for i in range(a):
    for j in range(b):
        y[i][j]=d[i][j]
for h in y:
    print(h)
    
for i in range(a):
    for j in range(b):
        result[i][j] = x[i][j] + y[i][j]
print("the sum of two matrices is")
for r in result:
    print(r)

    

