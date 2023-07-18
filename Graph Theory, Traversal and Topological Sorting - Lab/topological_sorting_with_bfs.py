from collections import deque


nodes = int(input())
graph = {}

for _ in range(nodes):
    line = input().split("->")
    node = line[0].strip()
    children = line[1].strip().split(", ") if line[1].strip() else []
    graph[node] = children

visited = set()
cycles = set()


def dfs(node, graph, visited, cycles, sorted_nodes):
    if node in cycles:
        raise Exception("Cycle has detected! Invalid topological sorting.")

    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.appendleft(node)


sorted_nodes = deque()
for node in graph:
    dfs(node, graph, visited, cycles, sorted_nodes)

print(*sorted_nodes, sep=" ")
