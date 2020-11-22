#https://www.hackerrank.com/challenges/xor-quadruples
def quad():
    a = [1, 2, 3, 4]
    n = len(a)
    output = []
    combinations = []    # Stores combinations
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    temp = [a[i], a[j], a[k], a[l]]
                    if (temp[0] <= a[0] and temp[1] <= a[1] and temp[2] <= a[2] and temp[3] <= a[3]):
                        temp.sort()
                        if(temp not in combinations):
                            combinations.append(temp)
                            if(a[i]^a[j]^a[k]^a[l] != 0):
                                output.append(temp)

    return len(output)



print(quad())