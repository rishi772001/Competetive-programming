height = input().split(" ")
alpha = ['a', 'b', 'c', 'remaining', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']
string = input()
length=len(string)
max=0
for i in string:
	if(int(height[alpha.index(i)])>max):
		max=int(height[alpha.index(i)])
print(max)