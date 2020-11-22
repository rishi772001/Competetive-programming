def truckTour(p):
    for _ in range(len(p)):
        i = _
        petrol = 0
        flag = True
        while(i < len(p)):
            petrol += p[i][0]
            if(p[i][1] < petrol):
                petrol -= p[i][1]
            else:
                flag = False
            i+=1
        i = len(p) % i
        while (i < _):
            petrol += p[i][0]
            if (p[i][1] < petrol):
                petrol -= p[i][1]
            else:
                flag = False
            i += 1
        if(flag):
            return _


if __name__ == '__main__':
    n = int(input())
    # n = 1
    # petrolpumps = [[1, 5], [10, 3], [3, 4]]
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    print(truckTour(petrolpumps))




