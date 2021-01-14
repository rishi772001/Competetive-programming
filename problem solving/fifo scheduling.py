'''
@Author: rishi
'''


class Solution:
    def averageWaitingTime(self, processes):
        wait_time = []

        start_time = 0
        for process in processes:
            if process[0] > start_time:
                start_time = process[0]

            wait_time.append(process[1] - process[0] + start_time)
            start_time += process[1]

        return sum(wait_time) / len(wait_time)
