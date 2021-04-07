'''
@Author: rishi
https://leetcode.com/problems/reaching-points/
'''


def recur(sx, sy, tx, ty):
    if sx > tx or sy > ty: return False
    if sx == tx: return (ty - sy) % sx == 0  # only change y
    if sy == ty: return (tx - sx) % sy == 0
    if tx > ty:
        return recur(sx, sy, tx % ty, ty)  # make sure tx%ty < ty
    elif tx < ty:
        return recur(sx, sy, tx, ty % tx)
    else:
        return False


print(recur(35, 13, 455955547, 420098884))
