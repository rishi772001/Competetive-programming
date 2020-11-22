'''
@Author: rishi
'''
def solve(s):
    a = s.split(".")
    if len(a) != 4:
        return False
    try:
        for i in a:
            if int(i) > 255 or int(i) < 0:
                return False
            if (len(i) > 1 and i[0] == '0') or i[0].isdigit() == False:
                return False
    except:
        return False
    return True

print(solve("0.1.2.+55"))