'''
@Author: rishi
'''


# Base class
class Employee(object):
    def __init__(self, eno, esal):
        self.__eno = eno
        self.__esal = esal

    def get(self):
        return self.__esal

    def set(self, esal):
        self.__esal = esal

    def increment(self, inc):
        self.__esal += inc
