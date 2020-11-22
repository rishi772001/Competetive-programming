def solve(lst, p):
    a = [0]*len(p)
    for i in range(len(p)):
        a[p[i]] = lst[i]
    return a

lst = ["a", "b", "c", "d"]
p = [3, 0, 1, 2]
print(solve(lst, p))