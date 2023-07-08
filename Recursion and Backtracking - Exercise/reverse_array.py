def reversed_array(starting_idx, numbers):
    if starting_idx == len(numbers) // 2:
        return

    swap_idx = len(numbers) - 1 - starting_idx
    numbers[starting_idx], numbers[swap_idx]= numbers[swap_idx], numbers[starting_idx]

    reversed_array(starting_idx + 1, numbers)



numbers = input().split()
reversed_array(0, numbers)
print(*numbers, sep=" ")


