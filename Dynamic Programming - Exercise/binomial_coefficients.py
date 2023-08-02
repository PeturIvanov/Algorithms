def find_bin_cof(n, k, memo):
    key = f"{n} {k}"
    if key in memo:
        return memo[key]

    if k == 0 or k == n:
        return 1

    result = find_bin_cof(n - 1, k - 1, memo) + find_bin_cof(n - 1, k, memo)
    memo[key] = result
    return result


n = int(input())
k = int(input())
print(find_bin_cof(n, k, {}))
