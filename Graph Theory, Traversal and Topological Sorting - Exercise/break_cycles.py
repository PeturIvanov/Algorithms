def path_exists(source, destination, multi_graph):
    visited = set()

    dfs(source, destination, multi_graph, visited)

    return destination in visited


def dfs(node, destination, multi_graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for child in multi_graph[node]:
        dfs(child, destination, multi_graph, visited)


nodes = int(input())
multi_graph = {}
edges = []
for _ in range(nodes):
    node, children = input().split(" -> ")
    children = children.split()
    multi_graph[node] = children
    for child in children:
        edges.append((node, child))


removed_edges = []
for source, destination in sorted(edges, key= lambda x: (x[0], x[1])):
    if source not in multi_graph[destination] or destination not in multi_graph[source]:
        continue

    multi_graph[source].remove(destination)
    multi_graph[destination].remove(source)

    if path_exists(source, destination, multi_graph):
        removed_edges.append((source, destination))
    else:
        multi_graph[source].append(destination)
        multi_graph[destination].append(source)


print(f"Edges to remove: {len(removed_edges)}")
for source, destination in removed_edges:
    print(f"{source} - {destination}")




