from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.source} - {self.destination} - {self.weight}"

    def __gt__(self, other):
        return self.weight > other.weight

nodes = int(input())
edges = int(input())
lightnings = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph[source].append(5)

    graph[source].append()
    graph[destination].append(Edge(destination, source, weight))

total_damage = 0
print(graph)
damage_taken = [0] * nodes

for lightning in range(lightnings):
    start, power = [int(x) for x in input().split()]

    visited = [False] * nodes
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        distance, node = pq.get()

        if not visited[node]:
            visited[node] = True
        else:
            continue

        damage_taken[node] += power
        power = power / 2

        for edge in graph[node]:
            pq.put((edge.weight, edge.destination))
            # print(distance, node)

print(damage_taken)
