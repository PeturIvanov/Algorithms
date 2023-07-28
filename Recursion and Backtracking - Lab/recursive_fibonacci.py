# def calc_fib(n):
#     if n <= 1:
#         return 1
#
#     return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_two(n):
    fib0 = 0
    fib1 = 1
    for _ in range(n - 1):
        fib0, fib1 = fib1, fib0 + fib1

    return fib1

n = int(input())
print(calc_fib_two(n))