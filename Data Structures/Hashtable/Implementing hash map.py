'''
@Author: rishi
'''


# Implement Hashmap without collision
class Hashmap:
    def __init__(self):
        self.MAXSIZE = 5
        self.arr = [None for i in range(self.MAXSIZE)]

    def find_hash(self, key):
        if type(key) == int:
            return (2*key+1)%self.MAXSIZE
        elif type(key) == str:
            s = 0
            for i in range(len(key)):
                s += ord(key)
            return s%self.MAXSIZE
        else:
            raise TypeError("Only integers or strings are allowed")

    def __setitem__(self, key, value):
        h = self.find_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.find_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.find_hash(key)
        self.arr[h] = None

    def __str__(self):
        return str(self.arr)

obj = Hashmap()
obj[1] = 10
obj[2] = 20
obj[3] = 30
obj["a"] = 1
del obj["a"]
print(obj[3])
print(obj)