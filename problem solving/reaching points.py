'''
@Author: rishi
'''
import sys

sys.setrecursionlimit(10 ** 6)


def recur(sx, sy, tx, ty):
    if sx == tx and sy == ty:
        return True
    if sx > tx or sy > ty:
        return False
    return recur(sx, sx + sy, tx, ty) or recur(sx + sy, sy, tx, ty)


print(recur(35, 13, 455955547, 420098884))
