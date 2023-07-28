from collections import deque

first_string = input()
second_string = input()

rows = len(first_string) + 1
cols = len(second_string) + 1

matrix = []

for _ in range(rows):
    matrix.append([0] * cols)

for row in range(1, rows):
    for col in range(1, cols):
        first = first_string[row - 1]
        second = second_string[col - 1]
        if first_string[row - 1] == second_string[col - 1]:
            matrix[row][col] = matrix[row - 1][col - 1] + 1


        else:
            matrix[row][col] = max(matrix[row - 1][col], matrix[row][col - 1])


print(matrix[rows - 1][cols - 1])

row = rows - 1
col = cols - 1
result = deque()

while row > 0 and col > 0:
    if first_string[row - 1] == second_string[col - 1]:
        result.appendleft(first_string[row - 1])
        row -= 1
        col -= 1

    elif matrix[row - 1][col] > matrix[row][col - 1]:
        row -= 1

    else:
        col -= 1

print(*result, sep=", ")
