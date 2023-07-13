def sorting_array(nums):
    is_sorted = False
    idx = 0

    while not is_sorted:
        is_sorted = True

        for j in range(1, len(nums) - idx):
            i = j -1
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                is_sorted = False

        idx += 1


nums = [int(x) for x in input().split()]
sorting_array(nums)
print(*nums, sep=" ")