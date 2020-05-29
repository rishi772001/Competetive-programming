input1=input().split(" ")
n=int(input1[0])
k=int(input1[1])
input2=input().split(" ")
b=int(input())
eat_no=input2[k]
eat=int(eat_no)

results=[]
for i in input2:
	results.append(i)
results = list(map(int, results))


sum=0
for i in results:
	sum+=i



c=sum
var_name=(c-eat)//2
var=b-var_name

if(var==0):
	print("Bon Appetit")
else:
	print(var)