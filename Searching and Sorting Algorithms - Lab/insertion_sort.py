def sort_array(nums):
    for idx in range(len(nums)):
        j = idx

        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1


nums = [int(x) for x in input().split()]
sort_array(nums)
print(*nums, sep=" ")