def num(s):
    for i in s:
        if(i.isnumeric()):
            return False
    return True

def low(s):
    for i in s:
        if(i.islower()):
            return False
    return True

def upp(s):
    for i in s:
        if(i.isupper()):
            return False
    return True

def spl(s):
    for i in s:
        if(i=='!'or i=='@'or i=='#'or i=='$'or i=='%'or i=='^'or i=='&'or i=='*'or i=='(' or i==')'or i=='-'or i=='+'):
            return False
    return True
c=0
a=input()
s=input()

if(num(s)):
    c+=1
    
if(low(s)):
    c+=1
    
if(upp(s)):
    c+=1
    
if(spl(s)):
    c+=1
    
if((len(s)+c)<6):
    c+=6-(len(s)+c)
print(c)
