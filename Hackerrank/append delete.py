s=input()

	
	
t=input()
k=int(input())
moves=0
final=""
'''for i in s:
	if(i not in t):
		s.remove(i)
		moves+=1
#print(s)
for j in t:
	if(j not in s):
		s.append(j)
		moves+=1
#print(s)'''
for i in range(len(s)):
	if(s in t):
		break
	else:
		s=s[:-1]
		moves+=1
final = final + t[(moves+1):]
moves+=len(final)
s=s+final
#print(s)
#print(moves)
if(moves==k):
	print("Yes")
else:
	print("No")