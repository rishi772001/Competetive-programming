# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
def median(arr):
    arr.sort()
    n=len(arr)
    print(arr)
    var = 0
    if(n%2==0):
        var = (arr[n//2]+arr[(n//2)+1])//2
        return var
    else:
        return arr[n//2]


def activityNotifications(exp, d):
    count = 0
    n = len(exp)
    for i in range(d,n):
        arr = exp[(i-d):i]
        if((median(arr)*2)<=exp[i]):
            count += 1
    return count

print(activityNotifications([2,3,4,2,3,6,8,4,5],5))