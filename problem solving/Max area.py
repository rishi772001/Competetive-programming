'''
@Author: rishi
'''


def getMaxArea(w, h, isVertical, distance):
    a = [[w, h]]
    ans = []
    for i in range(len(distance)):
        if isVertical[i] == 0:
            h1 = h - distance[i]
            h2 = distance[i]
            i = 0
            while i < len(a):
                if a[i][1] > distance[i]:
                    temp = a.pop(i)
                    a.insert(i,temp[:1] + [h1])
                    a.insert(i,temp[:1] + [h2])
                i += 2
        else:
            w1 = w - distance[i]
            w2 = distance[i]
            i = 0
            while i < len(a):
                if a[i][0] > distance[i]:
                    temp = a.pop(i)
                    a.insert(i,[w1] + temp[1:])
                    a.insert(i,[w2] + temp[1:])
                i += 2
        print(a)
        ans.append(max(i * j for i, j in a))
    return ans

print(getMaxArea(4,3,[1,1],[1,3]))