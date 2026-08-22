# 628. Maximum Product of Three Numbers
# Attempted
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24

# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6
 
# Constraints:
# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxi1=float("-inf")
        maxi2=float("-inf")
        maxi3=float("-inf")
        mini1=float("inf")
        mini2=float("inf")
        
        for i in range(len(nums)):
            if nums[i]<=mini1:
                mini2=mini1
                mini1=nums[i]
            elif nums[i]<=mini2:
                mini2=nums[i]

        for i in range(len(nums)):
            if nums[i]>=maxi1:
                maxi3=maxi2
                maxi2=maxi1
                maxi1=nums[i]
            elif nums[i]>=maxi2:
                maxi3=maxi2
                maxi2=nums[i]
            
            elif nums[i]>=maxi3:
                maxi3=nums[i]
        r1=maxi1 * maxi2 * maxi3
        r2=mini1 * mini2 * maxi1
        return r1 if r1>r2 else r2


# Time Complexity: O(n)
# Auxiliary Space: O(1)