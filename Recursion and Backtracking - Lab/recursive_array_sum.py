def sum_numbers(idx, numbers_aray):
    if idx == len(numbers_aray):
        return 0

    return numbers_aray[idx] + sum_numbers(idx + 1, numbers_aray)


numbers = [int(x) for x in input().split()]
print(sum_numbers(0, numbers))