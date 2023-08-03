from collections import deque

nums = [int(x) for x in input().split()]

dp = [[1] * len(nums) for _ in range(2)]
parents = [[None] * len(nums) for _ in range(2)]
dp[0][0] = dp[1][0] = 1

best_size = 0
best_col = 0
best_row = 0

for current in range(len(nums)):
    current_number = nums[current]

    for prev in range(current - 1, -1, -1):
        prev_number = nums[prev]

        if current_number > prev_number and dp[1][prev] + 1 >= dp[0][current]:
            dp[0][current] = dp[1][prev] + 1
            parents[0][current] = prev

        if current_number < prev_number and dp[0][prev] + 1 >= dp[1][current]:
            dp[1][current] = dp[0][prev] + 1
            parents[1][current] = prev

    if dp[0][current] > best_size:
        best_size = dp[0][current]
        best_col = current
        best_row = 0

    if dp[1][current] > best_size:
        best_size = dp[1][current]
        best_col = current
        best_row = 1

result = deque()

while best_col is not None:
    result.appendleft(nums[best_col])
    best_col = parents[best_row][best_col]
    best_row = 1 if best_row == 0 else 0

print(*result)

