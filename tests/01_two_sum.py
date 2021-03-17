def twoSum(nums, target):
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    """
    for i, num in enumerate(nums):
        # print(i, num)
        if target - num in nums[:i]:
            return [nums.index(target - num), i]

print(twoSum([3,3], 6))