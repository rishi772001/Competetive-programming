'''
@Author: rishi
https://leetcode.com/problems/maximize-distance-to-closest-person/
'''


def maxDistToClosest(seats):
    max_dist, start, end = 0, 0, 0

    curr = 0
    curr_start = 0
    for i in range(len(seats)):
        if seats[i] == 0:
            curr += 1
        else:
            if max_dist < curr:
                max_dist = curr
                end = i
                start = curr_start 
            curr_start = i
            curr = 0

    if max_dist < curr:
        max_dist = curr
        end = i
        start = curr_start

    print(start, end, max_dist)
    if end == len(seats) - 1 and seats[end] == 0:
        return end
    if start == 0:
        return 0

    return start + (end - start + 1) // 2

print(maxDistToClosest([1,0,1,0]))