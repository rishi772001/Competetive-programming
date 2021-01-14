'''
@Author: rishi
'''


def search(searchstr, l):
    ways = 0
    if searchstr == "":
        return 1
    else:
        for i in l:
            if i in searchstr:
                if searchstr.index(i) == 0:
                    cropedstr = searchstr[len(i):]
                    ways += search(cropedstr, l)
    return ways


s = input()
k = int(input())
l = []
for i in range(k):
    l.append(input())
ways = search(s, l)
print(ways)
