a=int(input("enter the no.of rows"))
b=int(input("enter the no.of columns"))
c=[[input("enter the element of matrix 1")for j in range(b)]for i in range(a)]
d=[[input("enter the element of matrix 2")for j in range(b)]for i in range(a)]
e=[[0 for j in range(b)]for i in range(a)]
x=[[0,0,0],[0,0,0],[0,0,0]]
y=[[0,0,0],[0,0,0],[0,0,0]]
z=[[0,0,0],[0,0,0],[0,0,0]]

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
    
print("sum of two matrices")

for i in range(a):
    for j in range(b):
        e[i][j]=c[i][j]+d[i][j]
        z[i][j]=e[i][j]
for j in z:
    print(j)

