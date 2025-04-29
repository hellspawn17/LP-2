from collections import deque

graph = {}

def add_edge(u, v):
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# Build graph
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('B', 'D')
add_edge('C', 'E')

print("Graph:")
print(graph)

# Recursive DFS
def dfs(visited, graph, root):
    if root not in visited:
        print(root, end=' ')
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)

# Recursive BFS
def bfs_recursive(visited, graph, queue):
    if not queue:
        return
    node = queue.popleft()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
    bfs_recursive(visited, graph, queue)

# Call DFS
print("\nDFS Traversal:")
visited = set()
dfs(visited, graph, 'A')

# Call BFS (Recursive)
print("\nBFS Traversal:")
visited = set()
queue = deque(['A'])
bfs_recursive(visited, graph, queue)
