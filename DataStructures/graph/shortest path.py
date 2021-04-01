graph = [['S', 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 1, 'E'],
        [0, 1, 0, 0, 1]]

n = 5  # size of graph

start_index = [0, 0]

for i in range(len(graph)):  # Find starting index
    if 'S' in graph[i]:
        start_index[0] = i
        start_index[1] = graph[i].index('S')
        break

visited = [[False]*n for i in range(n)]  # Create boolean array of visited array

queue = []  # queue FIFO
queue.append(start_index)   # Add element at end of array
visited[start_index[0]][start_index[1]] = True

dist = [[0]*n for i in range(n)]  # Create distance array
prev = [0,0]

while len(queue) > 0:         # BFS

    temp = queue.pop(0)
    prev = temp
    val = [[temp[0] - 1, temp[1]],  # All possible moves top, bottom, left, right
         [temp[0] + 1, temp[1]],
         [temp[0], temp[1]],
         [temp[0], temp[1] - 1],
         [temp[0], temp[1] + 1]]

    for i in val:
        if i[0] < 0 or i[1] < 0 or i[0] >= n or i[1] >= n or graph[i[0]][i[1]] == 0:  # Check for valid move
            continue
        if not visited[i[0]][i[1]]:
            dist[i[0]][i[1]] = dist[prev[0]][prev[1]] + 1
            if graph[i[0]][i[1]] == 'E':
                print("Reached in", dist[i[0]][i[1]],"steps")
                break  # Break all nested loops
            queue.append(i)
            visited[i[0]][i[1]] = True
    else:
        continue
    break



