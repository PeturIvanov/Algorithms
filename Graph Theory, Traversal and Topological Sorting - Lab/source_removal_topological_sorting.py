def find_dependency(graph):
    result = {}

    for node, children in graph.items():
        if node not in result:
            result[node] = 0

        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


def find_node_without_dependencies(nodes_dependency):
    for node, dependencies in nodes_dependency.items():
        if dependencies == 0:
            return node

    return None


nodes = int(input())
graph = {}

for _ in range(nodes):
    line = input().split("->")
    node = line[0].strip()
    children = line[1].strip().split(", ") if line[1].strip() else []
    graph[node] = children


nodes_dependency = find_dependency(graph)

sorted_nodes = []

while nodes_dependency:
    node_to_remove = find_node_without_dependencies(nodes_dependency)

    if not node_to_remove:
        print("Invalid topological sorting")
        exit()

    for child in graph[node_to_remove]:
        nodes_dependency[child] -= 1

    nodes_dependency.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)

print(f"Topological sorting: {', '.join(sorted_nodes)}")

