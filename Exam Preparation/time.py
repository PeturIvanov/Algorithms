from collections import deque

first_line = [int(x) for x in input().split()]
second_line = [int(x) for x in input().split()]

rows = len(first_line) + 1
cols = len(second_line) + 1
dp = [([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    first_number = first_line[row - 1]

    for col in range(1, cols):
        second_number = second_line[col - 1]

        if first_number == second_number:
            dp[row][col] = dp[row - 1][col - 1] + 1

        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

r, c = rows - 1, cols - 1
path = deque()
while r > 0 and c > 0:
    if first_line[r - 1] == second_line[c - 1]:
        path.appendleft(first_line[r - 1])
        r -= 1
        c -= 1

    elif dp[r - 1][c] >= dp[r][c - 1]:
        r -= 1
    else:
        c -= 1

print(*path, sep=" ")
print(dp[rows - 1][cols - 1])
