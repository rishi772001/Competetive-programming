def space(s):
	sp="";
	for i in range(s):
		sp+=" "
	return sp

s=input()
if(len(s)%2==0):
    s=s+"$"
rev=s[::-1]
n=((len(s)-2)*2)+1
half=(len(s)//2)
h=(half-1)*2
io=0
for i in range(len(s)):
    if(half>i):
        print(space(io)+str(s[i])+space(n)+str(rev[i]))
        n=n-4
        io=io+2
    elif(half==i):
        print(space(io)+str(s[i]))
        n=n+4
    else:
        print(space(h)+str(rev[i])+space(n)+str(s[i]))
        h=h-2
        n=n+4