'''
@Author: rishi
'''


def a(*args, **kwargs):
    print(args)
    print(kwargs)


a(1, name = "rishi")
a(1,2, name = "rishi", lname = "raj")