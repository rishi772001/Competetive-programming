def py():
    a=int(input("enter no.of.rows"))
    b=int(input("enter no.of.colums"))
    c=[[input("enter the elements")for j in range(a)]for i in range(b)]
    for i in range(a):
        for j in range(b):
            print (c[i][j])
        
