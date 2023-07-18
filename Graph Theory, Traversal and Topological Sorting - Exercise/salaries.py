def dfs(employee, graph, visited):
    result = 0

    if employee in visited:
        return result

    visited.add(employee)

    if not graph[employee]:
        result += 1

    for child in graph[employee]:
        result += dfs(child, graph, visited)

    visited.remove(employee)
    return result

employees = int(input())
graph = {}
total_salaries = 0

for e in range(employees):
    line = input()
    graph[e] = []

    for i in range(len(line)):
        if line[i] == "Y":
            graph[e].append(i)

visited = set()
for employee in graph:
    total_salaries += dfs(employee, graph, visited)

print(total_salaries)
