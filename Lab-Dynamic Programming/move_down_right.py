from collections import deque

rows = int(input())
cols = int(input())
matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        if dp[row][col - 1] >= dp[row - 1][col]:
            dp[row][col] = dp[row][col - 1] + matrix[row][col]

        else:
            dp[row][col] = dp[row - 1][col] + matrix[row][col]

row = rows - 1
col = cols - 1
path = deque()

while row > 0 and col > 0:
    path.appendleft([row, col])

    if dp[row][col - 1] >= dp[row - 1][col]:
        col -= 1

    else:
        row -= 1

for idx in range(row, 0, -1):
    path.appendleft([idx, col])

for idx in range(col, 0, -1):
    path.appendleft([row, idx])

path.appendleft([0, 0])

print(*path, sep=" ")
