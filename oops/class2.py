'''
@Author: rishi
'''

from oops.class1 import employee as emp

# inheritance
class emputil(emp):
    def __init__(self, name, eno, esal):
        self.__name = name
        super().__init__(eno, esal)

    # override base class method(polymorphism)
    def increment(self, inc, amt):
        curr = self.get()
        self.set(curr + inc + amt)

obj = emputil("rishi", 1, 100)
obj.increment(10, 10)
print(obj.get())
