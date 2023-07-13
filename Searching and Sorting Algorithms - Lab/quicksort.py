def qsort(start, end, nums):
    if start >= end:
        return

    pivot, left, right = start, start + 1, end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] <= nums[pivot]:
            left += 1

        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]

    qsort(start, right - 1, nums)
    qsort(right + 1, end, nums)


nums = [int(x) for x in input().split()]

qsort(0, len(nums) - 1, nums)
print(*nums, sep=" ")