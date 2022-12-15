def test(nums):
    return all([nums[i] != nums[i + 1] for i in range(len(nums)-1)]) and len(set(nums)) == 4
nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print("Original list:")
print(nums)
print("Check said list of integers containing exactly four distinct values, such that no integer repeats  twice consecutively:")
print(test(nums))