n=int(input("enter the number: "))
s=0
rev=0
large=0
while(n>0):
    rem=n%10
    s=s+rem
    rev=rem+(rev*10)
    if(rem>large):
        large=rem
    n=n//10
print("the sum of the digits",s)
print("the reverse of the digits=",rev)
print("the largest digit=",large)
