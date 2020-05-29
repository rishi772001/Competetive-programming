class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 

q=queue()


input1=input().split(" ")
n=input1[0]
k=input1[1]
arr=input().split(" ")
for i in arr:
	q.enqueue(i)

	q.dequeue()
