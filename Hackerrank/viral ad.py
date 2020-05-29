days=int(input())
count=0
shared=5
for i in range(days):
	shared=shared//2
	count+=shared
	shared=shared*3
print(count)