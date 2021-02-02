import math

n = int(input("enter the number of terms: "))
a = -1
b = 1
s = 0
print("the fibonacci series is : ")
for i in range(1, n + 1):
    c = a + b
    print(c, end="\t")
    s = s + c
    a = b
    b = c
print("\nthe sum of the series is :", s)

# nth value of fibonacci series
n = int(input("enter n: "))
temp = (1 + math.sqrt(5)) / 2
print(round(pow(temp, n) / math.sqrt(5)))
