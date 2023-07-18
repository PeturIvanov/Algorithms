def find_area(row, col, current_letter, letters, field):
    if 0 > row or row >= len(field) or 0 > col or col >= len(field[0]):
        return

    if current_letter == "v":
        return

    if field[row][col] != current_letter:
        return

    field[row][col] = "v"

    find_area(row, col + 1, current_letter, letters, field)
    find_area(row, col - 1, current_letter, letters, field)
    find_area(row + 1, col, current_letter, letters, field)
    find_area(row - 1, col, current_letter, letters, field)

rows = int(input())
cols = int(input())

field = [list(input()) for _ in range(rows)]
letters = {}

for r in range(rows):
    for c in range(cols):
        current_letter = field[r][c]
        if current_letter == "v":
            continue

        if current_letter not in letters:
            letters[current_letter] = 0

        letters[current_letter] += 1

        find_area(r, c, current_letter, letters, field)

total_areas = sum(letters.values())
print(f"Areas: {total_areas}")

for letter, value in sorted(letters.items()):
    print(f"Letter '{letter}' -> {value}")