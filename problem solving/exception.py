'''
@Author: rishi
'''


class InvalidAgeException(Exception):
    pass


a = int(input())

try:
    if a < 18:
        raise InvalidAgeException("message")
except InvalidAgeException:
    print("invalid age")

print("other program")
