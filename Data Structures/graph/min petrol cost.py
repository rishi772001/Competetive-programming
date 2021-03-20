'''
@Author: rishi
https://codeforces.com/blog/entry/45897

You want to travel from city A to city B.
There are N cities and M bidirectional roads connecting cities.
Your car can store up to C liters of fuel and the tank is initially full.
each road (i,j) has a value Wij that represents the amount of liters of fuel to cross this road.
Also, in every city you can buy fuel, at a price of Ci dollars per liter.
You must compute the minimum amount of dollars spent with fuel to travel from A to B.
'''
n = 4  # no of cities
m = 4  # no of roads
c = 4  # max capacity
petrol_cost = [1, 2, 3, 4]
roads = [
    [],
    [],
    []
]
