'''
@Author: rishi
https://binarysearch.com/problems/Run-Length-Encoding
'''


def encode(s):
    curr = ""
    curr_len = 0
    ans = ""
    for i in range(len(s)):
        if curr == "":
            curr = s[i]
            curr_len += 1
        elif curr == s[i]:
            curr_len += 1
        else:
            ans += str(curr_len) + s[i - 1]
            curr = s[i]
            curr_len = 1
    ans += str(curr_len) + s[i]
    return ans


def decode(s):
    ans = ""
    curr_char = ""
    curr_count = 0
    for i in s:
        if i.isdigit():
            curr_count = (curr_count * 10) + int(i)
        if i.isalpha():
            ans += curr_char * curr_count
            curr_char = i
            curr_count = 0
    ans += curr_char * curr_count
    return ans


print(encode("AAAABBBCCDAA"))
print(decode("A40B10"))
