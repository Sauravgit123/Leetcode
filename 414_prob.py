# 414. Third Maximum Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.



class Solution:
    def thirdMax(self, nums: List[int]) -> int:
       
        maxi1=float('-inf')
        maxi2=float('-inf')
        maxi3=float('-inf')
        for i in range(len(nums)):
            if nums[i]== maxi1 or nums[i]== maxi2 or nums[i]== maxi3:
                continue
            if nums[i]>maxi1:
                maxi3=maxi2
                maxi2=maxi1
                maxi1=nums[i]
    
            elif nums[i]>maxi2:
                maxi3=maxi2
                maxi2=nums[i]
            elif nums[i]>maxi3:
                maxi3=nums[i]

        if maxi3 == float('-inf'):
            return maxi1

        return maxi3
        







