class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.source} to {self.destination} = {self.weight}"

def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]

    return node


nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(" - ")]
    edge = Edge(source, destination, weight)
    graph.append(edge)

parent = [num for num in range(nodes)]
town = []

for edge in sorted(graph, key=lambda x: x.weight):
    source_root = find_root(parent, edge.source)
    destination_root = find_root(parent, edge.destination)

    if source_root != destination_root:
        parent[source_root] = destination_root
        town.append(edge)

total_cost = sum([edge.weight for edge in town])
print(f"Total cost: {total_cost}")

