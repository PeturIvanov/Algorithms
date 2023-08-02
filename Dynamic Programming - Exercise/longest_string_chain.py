from collections import deque

words = input().split()

chain_size = [0] * len(words)
prev = [None] * len(words)

best_idx = 0
best_size = 1

for current_idx in range(len(words)):
    current_word = words[current_idx]
    current_best_size = 1
    parent = None

    for prev_idx in range(current_idx - 1, -1, -1):
        prev_word = words[prev_idx]

        if len(prev_word) >= len(current_word):
            continue

        else:
            if chain_size[prev_idx] + 1 >= current_best_size:
                current_best_size = chain_size[prev_idx] + 1
                parent = prev_idx

    prev[current_idx] = parent
    chain_size[current_idx] = current_best_size

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = current_idx

result = deque()

while best_idx is not None:
    result.appendleft(words[best_idx])
    best_idx = prev[best_idx]

print(*result)
