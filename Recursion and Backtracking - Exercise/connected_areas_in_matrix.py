class Field:
    def __init__(self, r, c, size):
        self.row = r
        self.col = c
        self.size = size

def find_field_size(r, c, rows, cols, field):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return 0

    if field[r][c] != "-":
        return 0

    field[r][c] = "v"

    result = 1
    result += find_field_size(r, c + 1, rows, cols, field)  # Right
    result += find_field_size(r, c - 1, rows, cols, field)  # Left
    result += find_field_size(r + 1, c, rows, cols, field)  # Down
    result += find_field_size(r - 1, c, rows, cols, field)  # Up

    return result


rows = int(input())
cols = int(input())

field = [list(input()) for _ in range(rows)]

fields = []

for r in range(rows):
    for c in range(cols):
        size = (find_field_size(r, c, rows, cols, field))
        if size:
            fields.append(Field(r, c, size))

print(f"Total areas found: {len(fields)}")

for idx, field in enumerate(sorted(fields, key=lambda x: -x.size)):
    print(f"Area #{idx + 1} at ({field.row}, {field.col}), size: {field.size}")
