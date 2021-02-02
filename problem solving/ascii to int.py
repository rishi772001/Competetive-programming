'''
@Author: rishi
https://binarysearch.com/problems/ASCII-String-to-Integer
'''


class Solution:
    def solve(self, s):
        ans = 0
        curr = ""

        for i in s:
            # if found a digit add it to curr
            if i.isdigit():
                curr += i
            # else add to ans and reset
            else:
                if curr != "":
                    ans += int(curr)
                curr = ""

        # for last digit
        if curr != "":
            ans += int(curr)

        return ans


print(Solution().solve("11aa22bb"))
