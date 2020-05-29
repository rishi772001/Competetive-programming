#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
def reverse(n):
	rev=0
	while(n>0):
		rev=rev*10+(n%10)
		n=n//10
	return rev
inpit=input().split(" ")
i=int(inpit[0])
j=int(inpit[1])
k=int(inpit[2])
cnt=0
while(i<=j):
	if((i-(reverse(i)))%k==0):
		cnt+=1
	i+=1
print(cnt)
	





