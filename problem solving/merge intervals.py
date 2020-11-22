# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
    if not intervals:
        return []


    intervals.sort()
    result = []
    cleft, cright = intervals[0]

    for i in range(1, len(intervals)):
        left, right = intervals[i]
        if left <= cright:
            cright = max(cright, right)
        else:
            result.append([cleft, cright])
            cleft, cright = left, right

    result.append([cleft, cright])
    return result


print(merge([[1,4],[0,2],[3,5]]))