def fact_num(n):
    if n == 0:
        return 1

    return n * fact_num(n - 1)


n = int(input())
print(fact_num(n))