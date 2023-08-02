cables = [int(x) for x in input().split()]
other_side = [n for n in range(1, len(cables) + 1)]

rows = len(cables) + 1
cols = len(other_side) + 1

dp = []
for _ in range(rows):
    dp.append([0] * cols)

for row in range(1, rows):
    for col in range(1, cols):
        if cables[row - 1] == other_side[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1

        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(f"Maximum pairs connected: {dp[rows - 1][cols - 1]}")


