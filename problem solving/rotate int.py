'''
@Author: rishi
'''
def rotate(n):
    digit_count = len(str(n))
    n = (n % 10) * pow(10, digit_count - 1) + (n // 10);
    return n

print(rotate(123))