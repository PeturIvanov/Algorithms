from collections import deque


def find_path(target, parent):
    path = deque()
    node = target
    while node:
        path.appendleft(node)
        node = parent[node]

    return len(path) - 1


def find_parents(start, target, graph):
    visited = [False] * (max(graph.keys()) + 1)
    parent = [None] * (max(graph.keys()) + 1)

    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            return find_path(target, parent)

        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    return -1

nodes = int(input())
pairs = int(input())
graph = {}

for _ in range(nodes):
    source, destinations = input().split(":")
    source = int(source)
    graph[source] = [int(x) for x in destinations.split()]

for pair in range(pairs):
    start, target = [int(x) for x in input().split("-")]
    path = find_parents(start, target, graph)

    print(f"{{{start}, {target}}} -> {path}")
