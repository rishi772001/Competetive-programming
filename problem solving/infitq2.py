'''
@Author: rishi
'''

ans = set()


def permute(a):
    global ans
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            val = a[i:j + 1]

            temp = {}
            for k in val:
                if k in temp:
                    temp[k] += 1
                else:
                    temp[k] = 1
            flag = True
            for k in temp:
                if (temp[k] % 2 != 0):
                    flag = False
                    break
            if flag:
                ans.add("".join(val))


string = input()
n = len(string)
a = list(string)
permute(a)
ans = list(ans)
ans = sorted(ans, key=lambda x: (len(x), x))
out = ""
for i in ans:
    out += i
    out += ","
print(out[:-1])
