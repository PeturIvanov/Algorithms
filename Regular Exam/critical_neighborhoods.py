from queue import PriorityQueue
from collections import deque

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.source}-{self.destination}-{self.weight}"

    def __gt__(self, other):
        return self.destination > other.destination


edges = int(input())
graph = {}

for _ in range(edges):
    first_city, second_city, distance = input().split(" - ")
    distance = int(distance)

    if first_city not in graph:
        graph[first_city] = []

    if second_city not in graph:
        graph[second_city] = []


    graph[first_city].append(Edge(first_city, second_city, distance))
    graph[second_city].append(Edge(second_city, first_city, distance))


nodes = len(graph.keys())
closed_roads = input().split(",")
starting_city = input()
target_city = input()

parent = {node: None for node in graph.keys()}
distances = {node: float("inf") for node in graph.keys()}
distances[starting_city] = 0
pq = PriorityQueue()
pq.put((0, starting_city))


while not pq.empty():
    min_distance, city = pq.get()

    if city == target_city:
        break

    for road in graph[city]:
        if f"{road.source}-{road.destination}" in closed_roads:
            continue
        if f"{road.destination}-{road.source}" in closed_roads:
            continue

        new_distance = road.weight + min_distance

        if new_distance < distances[road.destination]:
            distances[road.destination] = new_distance
            parent[road.destination] = city
            pq.put((new_distance, road.destination))

path = deque()
node = target_city
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(*path, sep=" - ")
print(distances[target_city])


