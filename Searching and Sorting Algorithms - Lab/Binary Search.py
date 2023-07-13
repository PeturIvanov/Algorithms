def binary_search(target, nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid_inx = (left + right) // 2

        if target == nums[mid_inx]:
            return mid_inx

        if target < nums[mid_inx]:
            right = mid_inx - 1

        else:
            left = mid_inx + 1
    return -1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(target, nums))