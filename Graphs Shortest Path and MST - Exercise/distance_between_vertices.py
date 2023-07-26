from collections import deque


nodes = int(input())
pairs = int(input())
graph = {}

for _ in range(nodes):
    source, destinations = input().split(":")
    source = int(source)
    graph[source] = [int(x) for x in destinations.split()]


def find_parents(start, target, graph, visited, parent):

    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            return parent

        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node


def find_path(target, parent):
    path = deque()
    node = target
    while node:
        path.appendleft(node)
        node = parent[node]

    return len(path) - 1


for pair in range(pairs):
    start, target = [int(x) for x in input().split("-")]

    visited = [False] * (max(graph.keys()) + 1)
    parent = [None] * (max(graph.keys()) + 1)

    parent = find_parents(start, target, graph, visited, parent)
    data = (start, target)
    result = -1

    if parent:
        result = find_path(target, parent)

    print(f"{{{', '.join(str(x) for x in data)}}} -> {result}")
