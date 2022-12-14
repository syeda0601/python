def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3

nums = [19,19,15,5,5,5,1,2]
print("Original list:")
print(nums)
print("Check whether the length of the said list is 8 and fifth element occurs thrice in the said list. :")
print(test(nums))