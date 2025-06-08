from collections import deque
def bfs(graph,start):
    queue = deque([start])
    visited = set()
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    queue.append(adj)
    return visited
                    

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['F'],
    'D': [],
    'F': []
}

print(bfs(graph,'A'))
