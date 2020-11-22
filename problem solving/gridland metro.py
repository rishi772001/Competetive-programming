#https://www.hackerrank.com/challenges/gridland-metro/problem

def gridlandMetro(n, m, k, track):
    try:
        arr = [[0]*m for _ in range(n)]

        for i in range(k):
            for j in range(track[i][1],track[i][2]+1):
                arr[(track[i][0])-1][j-1]+=1

        count = 0
        for i in range(n):
            count+=arr[i].count(0)

        return count
    except RuntimeError as e:
        print(e.message)

    return count


if __name__ == '__main__':

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    print(gridlandMetro(n, m, k, track))