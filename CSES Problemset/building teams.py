'''
@Author: rishi
'''
from collections import defaultdict


n, m = map(int, input().split())
friendships = []
for _ in range(m):
    friendships.append(list(map(int, input().split())))
# out = team1 -> 1,4    team2 -> 2,3,5
friends = defaultdict(list)
for i,j in friendships:
    friends[i].append(j)
    # friends[j].append(i)

print(friends)
team1 = []
team2 = []

visited = {}
for i in range(1, n+1):
    visited[i] = False

for i in range(1, n+1):
    if not visited[i]:
        q = [i]
        flag = True  # add in team 1
        while q:
            s = len(q)
            for _ in range(s):
                temp = q.pop(0)
                visited[temp] = True
                if flag:
                    if temp not in team1:
                        team1.append(temp)

                else:
                    if temp not in team1:
                        team2.append(temp)


                for curr in friends[temp]:
                    q.append(curr)
            if flag:
                flag = False
            else:
                flag = True

print(team1, team2)
for i in range(1, n+1):
    if i in team1:
        print("1", end = " ")
    else:
        print("2", end=" ")