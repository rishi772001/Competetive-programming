class Stack:
    def __init__(self):
        self.values = []

    def push(self, data):
        self.values.append(data)

    def pop(self):
        return self.values.pop()

    def size(self):
        return len(self.values)


if __name__ == '__main__':
    dict = {'(': ')', '{': '}', '[': ']'}

    for _ in range(1):
        st = "{[](}([)(])[]]})()]){[({]}{{{)({}(][{{[}}(]{"
        s = Stack()
        flag = True
        for i in st:
            if i in '({[':
                s.push(i)
            if i in ')}]':
                if dict[s.pop()] != i:
                    flag = False
        if s.size() != 0:
            flag = False
        if (flag):
            print("YES")
        else:
            print("NO")
