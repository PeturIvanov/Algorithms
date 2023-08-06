from collections import deque

goals = [int(x) for x in input().split(", ")]

parent = [None] * len(goals)
size = [0] * len(goals)

best_size = 0
best_idx = 0

for current in range(len(goals)):
    current_best_size = 1
    current_parent = None

    for prev in range(current - 1, -1, -1):
        if goals[current] < goals[prev]:
            continue

        else:
            if size[prev] + 1 >= current_best_size:
                current_best_size = size[prev] + 1
                current_parent = prev

    size[current] = current_best_size
    parent[current] = current_parent

    if size[current] > best_size:
        best_size = size[current]
        best_idx = current

subsequence = deque()
while best_idx is not None:
    subsequence.appendleft(goals[best_idx])
    best_idx = parent[best_idx]

print(*subsequence, sep=" ")
