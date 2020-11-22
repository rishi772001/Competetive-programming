# https://leetcode.com/problems/triangle/

def triangle(ar):
    sum = ar[0][0]
    ind = 0
    for i in range(1, len(ar)):
        if ind == 0:
            if ar[i][ind] < ar[i][ind + 1]:
                sum += ar[i][ind]
            else:
                sum += ar[i][ind + 1]
                ind += 1
            continue

        if ind == len(ar) - 1:
            if ar[i][ind] < ar[i][ind - 1]:
                sum += ar[i][ind]
            else:
                sum += ar[i][ind - 1]
                ind -= 1
            continue

        if ar[i][ind] < ar[i][ind - 1]:

            if ar[i][ind] < ar[i][ind + 1]:
                sum += ar[i][ind]
            else:
                sum += ar[i][ind + 1]
                ind += 1
        else:
            if ar[i][ind + 1] < ar[i][ind - 1]:
                sum += ar[i][ind + 1]
                ind += 1
            else:
                sum += ar[i][ind - 1]
                ind -= 1



    return sum

print(triangle([[-1],[2,3],[1,-1,-3]]))