'''
@Author: rishi
'''


def solve(s, t):
    s_dict = {}
    t_dict = {}

    ans = 0

    for i in s:
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1

    for i in t:
        if i in t_dict:
            t_dict[i] += 1
        else:
            t_dict[i] = 1


    for i in s_dict:
        if i in t_dict:
            ans += max(0, s_dict[i] - t_dict[i])
        else:
            ans += s_dict[i]

    return ans


print(solve("ehyoe", "hello"))
