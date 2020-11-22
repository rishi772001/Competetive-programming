n=int(input("enter the number of terms: "))
a=-1
b=1
s=0
print("the fibonacci series is : ")
for i in range(1,n+1):
    c=a+b
    print(c,end="\t")
    s=s+c
    a=b
    b=c
print("\nthe sum of the series is :",s)
