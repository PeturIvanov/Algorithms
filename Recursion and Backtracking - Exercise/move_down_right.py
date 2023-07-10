def find_all_paths(r, c, rows, cols, field):
    global paths_count
    if 0 > r or r >= rows or 0 > c or c >= cols:
        return

    if field[r][c] == "v":
        return

    if field[r][c] == "e":
        paths_count += 1

    else:
        field[r][c] = "v"
        find_all_paths(r, c + 1, rows, cols, field)  # RIGHT
        find_all_paths(r + 1, c, rows, cols, field)  # DOWN
        field[r][c] = "-"

rows = int(input())
cols = int(input())

field = [list("-" * cols) for _ in range(rows)]
field[-1][-1] = "e"
paths_count = 0

find_all_paths(0, 0, rows, cols, field)
print(paths_count)
