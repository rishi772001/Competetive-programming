s="sabarirajj"
n=10
for i in range(n):
    if(i<=n//2):
        print(" "*(i) , end="")
        print(s[i] , end="")
        print(" "*(n-2*i) , end="")
        print(s[i])
    else:
        print(" "*(n-i) , end="")
        print(s[i] , end="")
        print(" "*abs(n-2*i) , end="")
        print(s[i])
          
    

