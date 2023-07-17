def dfs(node, graph, visited, result):
    if node in visited:
        return

    visited.append(node)

    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.append(node)

nodes = int(input())
graph = []

for _ in range(nodes):
    children = [int(c) for c in input().split()]
    graph.append(children)


visited = []
for node in range(len(graph)):
    if node in visited:
        continue

    result = []
    dfs(node, graph, visited, result)
    
    print(f"Connected component: {' '.join([str(x) for x in result])}")

