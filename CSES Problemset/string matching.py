'''
@Author: rishi
'''
string = input()
pattern = input()

size = len(pattern)
start = 0
end = start + size

res = 0

while end <= len(string):
    if string[start:end] == pattern:
        res += 1
    start += 1
    end += 1

print(res)
