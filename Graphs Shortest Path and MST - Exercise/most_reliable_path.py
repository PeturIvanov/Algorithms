from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.source} - {self.destination} == {self.weight}"

nodes = int(input())
edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    if source not in graph:
        graph[source] = []

    if destination not in graph:
        graph[destination] = []

    edge = Edge(source, destination, weight)
    graph[source].append(edge)
    graph[destination].append(edge)

start = int(input())
target = int(input())


distances = [float('-inf')] * nodes
distances[start] = 100

pq = PriorityQueue()
pq.put((-100, start))

parent = [None] * nodes

while not pq.empty():
    min_distance, node = pq.get()

    if node == target:
        break

    for edge in graph[node]:
        child = edge.destination if edge.source == node else edge.source
        new_distance = -min_distance * edge.weight / 100

        if new_distance > distances[child]:
            distances[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))


def find_path(target, parent):
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path

print(f"Most reliable path reliability: {distances[target]:.2f}%")
path = find_path(target, parent)
print(*path, sep=" -> ")
