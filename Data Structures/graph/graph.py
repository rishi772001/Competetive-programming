from collections import defaultdict

class graph:
    # Create a graph
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,start,end):
        self.graph[start].append(end)

    def printGraph(self):
        for i in self.graph:
            print(i,end=" = ")
            print(self.graph[i])

    def bfs(self,s):
        visited = [False]*(len(self.graph))

        queue = list()
        queue.append(s)
        visited[s] = True

        while (len(queue)>0):
            s = queue.pop(0)
            print(s," ")
            for i in self.graph[s]:
                if(visited[i]==False):
                    queue.append(i)
                    visited[i] = True


    def dfs(self,s):
        visited = [False] * (len(self.graph))

        stack = []
        stack.append(s)
        visited[s] = True

        while (len(stack)>0):
            s = stack.pop()
            print(s)
            for i in self.graph[s]:
                if (visited[i] == False):
                    stack.append(i)
                    visited[i] = True




g = graph()

g.addEdge(1,0)
g.addEdge(0,2)
g.addEdge(2,1)
g.addEdge(0,3)
g.addEdge(1,4)

g.printGraph()
print("bfs:")
# g.bfs(2)
print("dfs:")
g.dfs(0)

