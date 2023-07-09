# def is_not_valid(r, c, rows, cols):
#     if 0 > r >= rows and 0 > c >= cols:
#         return True
#
#     if field[r][c] == 'v':
#         return True
#
#     return False

def find_all_paths(r, c, rows, cols, field, paths):
    if 0 > r >= rows and 0 > c >= cols:
        return

    if field[r][c] == "v":
        return

    if field[r][c] == "e":
        paths += 1

    else:
        field[r][c] = "v"
        find_all_paths(r, c + 1, rows, cols, field, paths_count)  # RIGHT
        find_all_paths(r + 1, c, rows, cols, field, paths_count)  # DOWN
        field[r][c] = "-"

    return paths



rows = int(input())
cols = int(input())

field = [list("-" * cols) for _ in range(rows)]
field[-1][-1] = "e"
paths_count = 0

paths_count = (find_all_paths(0, 0, rows, cols, field, paths_count))
print(paths_count)
