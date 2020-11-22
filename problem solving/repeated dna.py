'''
@Author: rishi
https://leetcode.com/problems/repeated-dna-sequences/
'''


def findRepeatedDnaSequences(s):
    if len(s) <= 10:
        return []
    a = set()
    ans = set()
    for i in range(len(s) - 9):
        if s[i:i + 10] in a:
            ans.add(s[i:i + 10])
        else:
            a.add(s[i:i + 10])
    return list(ans)

findRepeatedDnaSequences("AAAAAAAAAAA")