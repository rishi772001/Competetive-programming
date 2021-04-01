# Difference between depth first search & breadth first search:

# BFS looks at each adjacent node and doesn't consider the children of those adjacent nodes.

# DFS looks at each adjacent node, and looks at all the children of the current adjacent nodes.
# It again, looks at the children of the next adjacent node (adjacent to the children of the previous).


from collections import defaultdict

class graph:
    # Create a graph
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self,start,end):
        self.graph[start].append(end)
        self.graph[end].append(start)  #For undirected graph


    def printGraph(self):
        for i in self.graph:
            print(i,end=" = ")
            print(self.graph[i])

    def bfs(self,s):
        visited = [False]*(self.v)

        queue = list()
        queue.append(s)
        visited[s] = True

        while (len(queue)>0):
            s = queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if(visited[i]==False):
                    queue.append(i)
                    visited[i] = True


    def dfs(self,s):
        visited = [False] * self.v
        stack = []
        stack.append(s)
        visited[s] = True

        while len(stack)>0:
            s = stack.pop()
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True







g = graph(5)

g.addEdge(1, 0);
g.addEdge(0, 2);
g.addEdge(2, 1);
g.addEdge(0, 3);
g.addEdge(1, 4);

g.printGraph()
print("bfs:")
g.bfs(0)
print("\ndfs:")
g.dfs(0)

