'''
@Author: rishi
'''


class Solution:
    def countStudents(self, students, sandwiches):
        # students = [1,1,1], sandwiches = [0,1,1] unable = 3
        unable = 0

        while len(students) > 0 and unable < len(students):
            stud = students.pop(0)
            if stud == sandwiches[0]:
                sandwiches.pop(0)
                unable = 0
            else:
                students.append(stud)
                unable += 1

        return unable
