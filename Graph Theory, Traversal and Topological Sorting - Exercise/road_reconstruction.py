# def dfs(source, destination, city, visited):
#     if source in visited:
#         return
#
#     visited.add(source)
#
#     if source == destination:
#         return
#
#     for building in city[source]:
#         dfs(building, destination, city, visited)
#
#
# def is_important(source, destination, city):
#     visited = set()
#
#     dfs(source, destination, city, visited)
#
#     return destination not in visited
#
#
# buildings = int(input())
# number_of_streets = int(input())
#
# city = {}
# streets = []
# important_streets = []
#
# for _ in range(number_of_streets):
#     first_building, second_building = input().split(" - ")
#     streets.append((first_building, second_building))
#
#     if first_building not in city:
#         city[first_building] = []
#
#     if second_building not in city:
#         city[second_building] = []
#
#     city[second_building].append(first_building)
#     city[first_building].append(second_building)
#
#
# for source, destination in streets:
#     if source not in city[destination] or destination not in city[source]:
#         continue
#
#     city[source].remove(destination)
#     city[destination].remove(source)
#
#     if is_important(source, destination, city):
#         important_streets.append((source, destination))
#
#     else:
#         city[source].append(destination)
#         city[destination].append(source)
#
# result = ["Important streets:"]
# for street in important_streets:
#     building1, building2 = sorted(street)
#     result.append(f"{building1} {building2}")
#
# print('\n'.join(result))

# Second solution:

buildings_count = int(input())
streets_count = int(input())

city = []
[city.append([]) for _ in range(buildings_count)]

streets = []

for _ in range(streets_count):
    first, second = [int(x) for x in input().split(" - ")]
    city[first].append(second)
    city[second].append(first)
    streets.append((min(first, second), max(first, second)))


print("Important streets:")


def dfs(building, city, visited):
    if visited[building]:
        return

    visited[building] = True

    for child in city[building]:
        dfs(child, city, visited)


for first, second in streets:
    city[first].remove(second)
    city[second].remove(first)

    visited = [False] * buildings_count
    dfs(0, city, visited)

    if not all(visited):
        print(first, second)

    city[first].append(second)
    city[second].append(first)















