st=input()
op=''
i=1
while(i<len(st)):
    op=op+st[i]
    i+=2
a=len(st)-len(op)
var=chr((ord(st[len(st)-1])))
if(var=='z'):
    var='a'
else:
    var=chr((ord(st[len(st)-1]))+1)
for i in range(a):
    op=op+var
print("op:",op)

