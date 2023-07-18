graph = {}
while True:
    input_line = input()
    if input_line == "End":
        break

    parent, child = input_line.split("-")

    if parent not in graph:
        graph[parent] = []

    graph[parent].append(child)

is_cyclic = True
visited = []
for node, children in graph.items():
    visited.append(node)

    for child in children:
        if child in visited:
            is_cyclic = False

if is_cyclic:
    print("Acyclic: Yes")

else:
    print("Acyclic: No")



# Second solution with dfs:

# graph = {}
# while True:
#     input_line = input()
#     if input_line == "End":
#         break
#
#     parent, child = input_line.split("-")
#
#     if parent not in graph:
#         graph[parent] = []
#
#     graph[parent].append(child)
#
#     if child not in graph:
#         graph[child] = []
#
# visited = set()
# cycle = set()
#
#
# def dfs(node, graph, visited, cycle):
#     if node in cycle:
#         print("Acyclic: No")
#         exit()
#
#     if node in visited:
#         return
#
#     visited.add(node)
#     cycle.add(node)
#
#     for child in graph[node]:
#         dfs(child, graph, visited, cycle)
#
#     cycle.remove(node)
#
# for node in graph:
#     dfs(node, graph, visited, cycle)
#
# print("Acyclic: Yes")
