from queue import PriorityQueue
from collections import deque


def find_path(target, parent):
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    return path


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.source}, {self.destination}, {self.weight}"


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(", ")]
    if source not in graph:
        graph[source] = []

    if destination not in graph:
        graph[destination] = []

    graph[source].append(Edge(source, destination, weight))

start = int(input())
target = int(input())

nodes = max(graph.keys())

parent = [None] * (nodes + 1)
distances = [float('inf')] * (nodes + 1)

pq = PriorityQueue()
pq.put((0, start))
distances[start] = 0

while not pq.empty():
    min_distance, node = pq.get()

    if node == target:
        break

    for edge in graph[node]:
        new_distances = edge.weight + min_distance

        if new_distances < distances[edge.destination]:
            distances[edge.destination] = new_distances
            parent[edge.destination] = node
            pq.put((new_distances, edge.destination))

if distances[target] == float('inf'):
    print("There is no such path.")

else:
    path = find_path(target, parent)
    print(distances[target])
    print(*path, sep= " ")

