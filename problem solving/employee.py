'''
@Author: rishi
'''


class Employee:
    def __init__(self, id, name, dept, sal):
        self.id = id
        self.name = name
        self.dept = dept
        self.sal = sal


a = [Employee(1, "abc", "a", 100),
     Employee(2, "abd", "a", 100),
     Employee(3, "xyz", "a", 300),
     Employee(4, "xyd", "a", 300)]

a = sorted(a, key=lambda p: (p.sal, p.name))
for i in a:
    print(i.name)
