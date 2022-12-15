#License: https://bit.ly/3oLErEI
 
def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])
nums = [1,1,1,1,1,1]
print("\nOriginal list:")
print(nums)
print("Check the said list, where the sum of the first i integers is i:")
print(test(nums))

