'''
@Author: rishi
https://leetcode.com/problems/my-calendar-i/
'''
import sys
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        for s, e in self.events:
            if s < end and start < e:
                return False
        self.events.append((start, end))
        return True


a = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
obj = MyCalendar()
for i in a:
    print(obj.book(i[0], i[1]))