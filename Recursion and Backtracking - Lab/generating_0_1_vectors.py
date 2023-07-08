def gen_vector(idx, result):
    if idx == len(result):
        print("".join([str(x) for x in result]))
        return

    for num in range(2):
        result[idx] = num
        gen_vector(idx + 1, result)

n = int(input())
result = [0] * n
gen_vector(0, result)