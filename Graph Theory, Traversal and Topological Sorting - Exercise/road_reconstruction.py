def dfs(source, destination, city, visited):
    if source in visited:
        return

    visited.add(source)

    if source == destination:
        return

    for building in city[source]:
        dfs(building, destination, city, visited)


def is_important(source, destination, city):
    visited = set()

    dfs(source, destination, city, visited)

    return destination not in visited


buildings = int(input())
number_of_streets = int(input())

city = {}
streets = []
important_streets = []

for _ in range(number_of_streets):
    first_building, second_building = input().split(" - ")
    streets.append((first_building, second_building))

    if first_building not in city:
        city[first_building] = []

    if second_building not in city:
        city[second_building] = []

    city[second_building].append(first_building)
    city[first_building].append(second_building)


for source, destination in streets:
    if source not in city[destination] or destination not in city[source]:
        continue

    city[source].remove(destination)
    city[destination].remove(source)

    if is_important(source, destination, city):
        important_streets.append((source, destination))

    else:
        city[source].append(destination)
        city[destination].append(source)

result = ["Important streets:"]
for street in important_streets:
    building1, building2 = sorted(street)
    result.append(f"{building1} {building2}")

print('\n'.join(result))

