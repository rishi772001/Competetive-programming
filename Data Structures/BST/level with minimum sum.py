'''
@Author: rishi
Keep tracking levels is the speciality of this
'''

class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return self.val


root = node(10)
root.left = node(2)
root.right = node(3)
root.right.left = node(4)
root.right.right = node(5)


q = list()
q.append(root)

min_val = 2147483647
level = 0
out = 0

# Run loop until q is empty that is no more nodes to process
while q:

    print()
    for i in q:
        print(i.val, end = ",")


    size = len(q)
    curr_sum = 0

    for i in range(size):       # Add children of current level to q and pop current level elements
        p = q.pop(0)
        curr_sum += p.val

        if p.left is not None:
            q.append(p.left)
        if p.right is not None:
            q.append(p.right)

    if curr_sum < min_val:
        min_val = curr_sum
        out = level

    level += 1

print()
print(out)