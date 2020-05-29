def calc(str):
	s="".join(set(str))
	sa=list(s)
	return sa
n=int(input())
op=""
ar=[]
for i in range(n):
	a=calc(input())
	for i in a:
		ar.append(i)
for i in ar:
	if((ar.count(i))>=2):
		op+=i
		ar.remove(i)
st="".join(set(op))
st=''.join(sorted(st))
print(st)