def print_nested_loops(idx, n, combination):
    if idx >= len(combination):
        print(*combination, sep=" ")
        return

    for num in range(1, n + 1):
        combination[idx] = num
        print_nested_loops(idx + 1, n, combination)


num = int(input())
combination = [0] * num
print_nested_loops(0, num, combination)
