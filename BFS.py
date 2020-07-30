from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph= defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        output = []
        visited = [False] * len(self.graph)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            output.append(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
        return output

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print(g.BFS(0))
