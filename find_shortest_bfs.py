# Define graph as an adjacency list
from collections import deque
def bfs(graph,node,goal):
    queue = deque([[node]])
    visited = set()  
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for adj in graph[node]:
                newpath= list(path)
                newpath.append(adj)
                queue.append(newpath)
                
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A','F'))
