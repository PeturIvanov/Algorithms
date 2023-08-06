def find_shortest_path(row, col, matrix, size,current_path):
    global shortest_path
    if 0 > row or row >= size or 0 > col or col >= size:
        return

    if matrix[row][col] == "#":
        return

    if matrix[row][col] == "v":
        return

    if matrix[row][col] == "E":
        if current_path < shortest_path:
            shortest_path = current_path


    else:
        matrix[row][col] = "v"
        current_path += 1
        find_shortest_path(row, col + 1, matrix, size, current_path)
        find_shortest_path(row + 1, col, matrix, size, current_path)
        find_shortest_path(row - 1, col, matrix, size, current_path)
        find_shortest_path(row, col - 1, matrix, size, current_path)
        matrix[row][col] = "."


size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

rows = size
cols = size
shortest_path = float("inf")
current_path = 0
find_shortest_path(0, 0, matrix, size, current_path)
print(shortest_path)
