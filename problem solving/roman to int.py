'''
@Author: rishi
'''


def solve(self, numeral):
    int_val = 0
    d = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    int_val += d[numeral[-1]]

    for i in range(len(numeral) - 2, -1, -1):

        if d[numeral[i]] < d[numeral[i + 1]]:
            int_val -= d[numeral[i]]
        else:
            int_val += d[numeral[i]]

    return int_val