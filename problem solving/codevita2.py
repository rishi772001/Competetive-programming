n=int(input())
input_rate=input().split(" ")
r1=int(input_rate[0])
r2=int(input_rate[1])
revenue=int(input())
calc=0
for i in range(n):
    calc+=r1
    if(calc>revenue):
        break
print(i)
