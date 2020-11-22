'''
@Author: rishi
'''


def solve(words):
    s = set()
    ans = 0
    for i in words:
        if i not in s:
            ans += 1
            # Add all rotations of that string to set
            for j in range(len(i)):
                s.add(i[j:] + i[:j])
    return ans

# Find how many rotation groups possible

# xy - yx
# abc - bca
# z

print(solve(["abc", "xy", "yx", "z", "bca"]))