from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"node {self.source} to {self.destination} weight {self.weight}"

nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start_node = int(input())
target_node = int(input())

parent = [None] * (nodes + 1)
distance = [float('inf')] * (nodes + 1)
distance[start_node] = 0


for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue

        new_distance = distance[edge.source] + edge.weight

        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True

    if not updated:
        break

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print("Negative Cycle Detected")
        break

else:
    path = deque()
    node = target_node

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=" ")
    print(distance[target_node])
