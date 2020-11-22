# https://leetcode.com/problems/cinema-seat-allocation/

n = 2
booked = [[1,6],[1,8],[1,3],[2,3],[1,10],[1,2],[1,5],[2,2],[2,4],[2,10],[1,7],[2,5]]

theatre = [[0]*10 for i in range(n)]

for i in range(len(booked)):
    theatre[booked[i][0] - 1][booked[i][1] - 1] += 1

print(theatre)
count = 0

for i in range(len(theatre)):
    sum = theatre[i][1] + theatre[i][2] + theatre[i][3] + theatre[i][4]
    j = 5
    flag = False
    if sum == 0:

        count += 1
        sum = theatre[i][j] + theatre[i][j + 1] + theatre[i][j + 2] + theatre[i][j + 3]
        j = j + 3
    while j < 10:
        if j - 4 == 1 or j - 4 == 3 or j - 4 == 5:

            sum += theatre[i][j]
            sum -= theatre[i][j - 4]


            j += 1
            continue
        if (sum == 0):

            count += 1
            if(j + 4 < 10):
                sum = theatre[i][j] + theatre[i][j + 1] + theatre[i][j + 2] + theatre[i][j + 3]
                j += 3
            else:
                break

        sum += theatre[i][j]
        sum -= theatre[i][j - 4]

        j += 1





print(count)

