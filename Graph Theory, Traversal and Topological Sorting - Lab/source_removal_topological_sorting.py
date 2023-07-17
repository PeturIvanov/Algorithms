def find_dependencies(graph):
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


dependencies_by_node = find_dependencies(graph)

sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_node_without_dependencies(dependencies_by_node)

    if not node_to_remove:
        print("Invalid topological sorting")
        exit()

    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)

print(f"Topological sorting: {', '.join(sorted_nodes)}")

