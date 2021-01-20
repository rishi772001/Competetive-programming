'''
@Author: rishi
'''
import sys


def eggdrop(eggs, floors):
    if eggs == 1:
        return floors
    if floors == 1:
        return 1

    mini = sys.maxsize
    for i in range(1, floors):
        mini = min(mini, max(eggdrop(eggs - 1, i - 1), eggdrop(eggs, floors - i)))
    return 1 + mini


eggs = 2
floors = 10
print(eggdrop(eggs, floors))
