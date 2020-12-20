n = int(input())
array = []
for i in range(n):
    array.append(int(input("enter")))
for i in array:
    if ((i % 5) >= 3):
        if (i < 38):
            print(i)
        else:
            print(i + (i % 5) - 1)

    else:
        print(i)
