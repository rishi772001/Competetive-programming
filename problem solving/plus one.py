# https://leetcode.com/problems/plus-one/

def plus(a):
    if(a[-1] != 9):
        if(len(a)==1 and a[0] == 9):
            a = [1] + a
        a[-1] += 1
        return a
    else:
        if(len(a) == 1):
            a[0] = 0
            a = [1] + a
            return a
        i = -1
        while i >= -(len(a)) and a[i] == 9:
            a[i]=0
            i -= 1
        if(i < -len(a)):
            i += 1
            if a[i] == 0:
                a[i] = 0
                a = [1] + a
            else:
                a[i] += 1
        else:
            a[i] += 1
            # a[-1] += 1
        return a

def shortcut(a):
    s = ""
    for i in a:
        s += str(i)
    s = int(s)
    s += 1
    s = str(s)
    a = list(map(int, s))
    return a




a = [9,9]
print(shortcut(a))

