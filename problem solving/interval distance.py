'''
@Author: rishi
'''


def solve(intervals):
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

    i = 0
    while i < len(intervals) - 1:

        if intervals[i][1] >= intervals[i + 1][0]:
            print(i)
            intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])

            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])

            intervals.pop(i + 1)

        else:
            i += 1

        print(intervals)

    ans = 0
    for i, j in intervals:
        ans += j - i + 1
    return ans


print(solve(intervals=[
    [45, 60],
    [1, 5],
    [5, 15],
    [2, 3]
]))
