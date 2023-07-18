def dfs(row, col, parent, visited, field):
    if 0 > row or row >= len(field) or 0 > col or col >= len(field[0]):
        return

    if visited[row][col]:
        return

    if field[row][col] != parent:
        return

    visited[row][col] = True

    dfs(row, col + 1, parent, visited, field)
    dfs(row, col - 1, parent, visited, field)
    dfs(row + 1, col, parent, visited, field)
    dfs(row - 1, col, parent, visited, field)

rows = int(input())
cols = int(input())

field = []
visited = []
for _ in range(rows):
    field.append(list(input()))
    visited.append([False] * cols)

letters = {}

for r in range(rows):
    for c in range(cols):
        key = field[r][c]

        if visited[r][c]:
            continue

        dfs(r, c, key, visited, field)

        if key not in letters:
            letters[key] = 0

        letters[key] += 1

total_areas = sum(letters.values())
print(f"Areas: {total_areas}")

for letter, value in sorted(letters.items()):
    print(f"Letter '{letter}' -> {value}")
