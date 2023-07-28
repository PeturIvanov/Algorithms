n = int(input())


def calc_fib(n, cache):
    if n in cache:
        return cache[n]

    if n <= 2:
        return 1

    result = calc_fib(n - 1, cache) + calc_fib(n - 2, cache)
    cache[n] = result
    return result


print(calc_fib(n, {}))