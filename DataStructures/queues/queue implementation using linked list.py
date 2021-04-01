'''
@Author: rishi
'''

from DataStructures.util.Node import Node


class EmptyQueueException(Exception):
    pass


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        if not self.front and not self.rear:
            self.front = self.rear = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next

    def dequeue(self):
        if not self.front and not self.rear:
            raise EmptyQueueException("Queue is empty")
        else:
            temp = self.front.val
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# Run time exception
print(q.dequeue())
