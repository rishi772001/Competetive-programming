#https://www.hackerrank.com/challenges/the-birthday-bar/
from itertools import combinations


# Complete the birthday function below.

def birthday(s, d, m):
    count=0
    if(len(s)==m):
        #if(sum(s)==d):
        return 1
    for i in range(len(s)-m):
        temp=s[i:i+m]
        if(sum(temp)==d):
            count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

