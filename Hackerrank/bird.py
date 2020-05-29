#https://www.hackerrank.com/challenges/migratory-birds/
def most_frequent(List): 

    return max(set(List), key = List.count) 
n=input()
s=input().split(" ")
ar=[]
for i in s:
	ar.append(int(i))

print(most_frequent(ar))
