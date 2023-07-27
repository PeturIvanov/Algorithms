from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        return f"{self.source} -> {self.destination} = {self.cost}"

    def __gt__(self, other):
        return self.cost > other.cost


budget = int(input())
nodes = int(input())
edges = int(input())
graph = {}


cable_connection = []
customers = set()

for _ in range(edges):
    input_data = input().split()
    first, second, cost = [int(x) for x in input_data[:3]]
    connection = True if "connected" in input_data else False

    if first not in graph:
        graph[first] = []

    if second not in graph:
        graph[second] = []

    edge = Edge(first, second, cost)
    graph[first].append(edge)
    graph[second].append(edge)

    if connection:
        cable_connection.append(edge)
        customers.update((first, second))


def prim(graph, customers, cable_connection, budget):
    result = 0

    pq = PriorityQueue()
    for customer in customers:
        for cable in graph[customer]:
            pq.put(cable)

    while not pq.empty():
        min_cable = pq.get()
        non_connected_customer = -1

        if min_cable.destination in customers and min_cable.source not in customers:
            non_connected_customer = min_cable.source

        elif min_cable.source in customers and min_cable.destination not in customers:
            non_connected_customer = min_cable.destination

        if non_connected_customer == -1:
            continue

        if min_cable.cost + result > budget:
            return result

        result += min_cable.cost
        customers.add(non_connected_customer)
        cable_connection.append(min_cable)

        for cable in graph[non_connected_customer]:
            pq.put(cable)

    return result


result = prim(graph, customers, cable_connection, budget)
print(f"Budget used: {result}")
