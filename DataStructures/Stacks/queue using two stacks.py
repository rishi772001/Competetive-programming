'''
@Author: rishi
'''


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # making enqueue operation costly
    def enqueue(self, element):
        # remove all elements from stack1 and temporarily store in stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # insert element
        self.stack1.append(element)
        # and copy all elements back to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.stack1:
            return self.stack1.pop()
        else:
            return -1


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
