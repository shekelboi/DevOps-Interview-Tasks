def sum_to_n(nums: list[int], target: int) -> list[int]:
    for start in range(len(nums)):
        for end in range(start + 1, len(nums) + 1):
            subarray = nums[start:end]
            if sum(subarray) == target:
                return subarray
    return subarray


nums = [1, 4, 0, 0, 3, 10, 5, 2, 1]
target_sum = 7
print(sum_to_n(nums, target_sum))
