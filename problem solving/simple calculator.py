def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    return x / y


def power(x, y):
    return x ** y


import math


def log(x, y):
    return math.log10(x)


def sqrt(x, y):
    return math.sqrt(x)


def fact(x, y):
    return math.factorial(x)


print("select the operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.power")
print("6.log")
print("7.square root")
print("8.factorial")
choice = input("enter the choice(1/2/3/4/5/6/7/8):")
print(
    "if choices are 6,7,8,9,10,11 then enter 2nd number as 0 and 1st number as the value for which you need the function")
num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
if (choice == "1"):
    print(add(num1, num2))
elif (choice == "2"):
    print(sub(num1, num2))
elif (choice == "3"):
    print(multiply(num1, num2))
elif (choice == "4"):
    print(division(num1, num2))
elif (choice == "5"):
    print(power(num1, num2))
elif (choice == "6"):
    print(log(num1, num2))
elif (choice == "7"):
    print(sqrt(num1, num2))
elif (choice == "8"):
    print(fact(num1, num2))
else:
    print("invalid input")
