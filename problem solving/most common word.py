def equal(a,b):
    count = 0
    if len(a) == len(b):
        for i in range(len(a)):
            if ((a[i] == b[i]) or (chr(ord(a[i]) + 32) == b[i]) or (chr(ord(b[i]) + 32) == a[i]) or (
                    chr(ord(a[i]) - 32) == b[i]) or (chr(ord(b[i]) - 32) == a[i])) and count < 2:
                if (a[i] != b[i]):
                    count += 1

            else:
                return False
        return True
    else:
        return False


s = input("Enter:")
s = s.split(" ")
norepeat = []
for i in s:
    flag=1
    for j in norepeat:
        if equal(i,j):
            flag=0
    if flag==1:
        norepeat.append(i)
dict={}
for i in norepeat:
    dict[i] = 0

for i in norepeat:
    for j in s:
        if equal(i,j):
            dict[i]+=1
m=max(dict, key=lambda x: dict[x])
print(dict)
for i in dict:
    if dict[i] == dict[m]:
        print(i, end=" ")




'''
dict = {}
for i in s:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
m=max(dict,key= lambda x: dict[x])

for i in dict:
    if(dict[i]==dict[m]):
        print(i, end=" ")
'''
#second
'''
ans=""
max = 0
for i in s:
    if(i not in ans and s.count(i)>max):
        ans=i
        max=s.count(i)
print(ans)
'''
#third