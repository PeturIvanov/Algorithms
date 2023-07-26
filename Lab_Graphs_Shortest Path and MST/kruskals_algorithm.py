class Edge:
    def __init__(self, first, second, weight):
        self.weight = weight
        self.second = second
        self.first = first

    def __repr__(self):
        return f"source {self.first} destination {self.second} weight {self.weight}"

def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]

    return node

edges = int(input())
graph = []

max_node = float('-inf')
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(", ")]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

parent = [num for num in range(max_node + 1)]
forest = []

for edge in sorted(graph, key=lambda x: x.weight):
    source_root = find_root(parent, edge.first)
    destination_root = find_root(parent, edge.second)

    if source_root != destination_root:
        parent[source_root] = destination_root
        forest.append(edge)

    else:
        print("have same root")

for edge in forest:
    print(f"{edge.first} - {edge.second}")
