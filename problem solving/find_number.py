'''
@Author: rishi
'''
a = input()
num = []
for i in a:
    if i.isnumeric():
        p = int(i)
        if p not in num:
            num.append(p)
if not len(num):
    print("No integers")
    exit(0)
for i in sorted(num):
    print(i, end="")
