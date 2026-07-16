# 34. Find First and Last Position of Element in Sorted Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums sorted in non-decreasing order,
#  find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        lb=len(nums)
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        low=0
        high=len(nums)-1
        ub=len(nums)
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return [lb,ub-1]
    
            
# Time Complexity: O(log n)
# (2 binary searches → O(log n) + O(log n) = O(log n))
# Space Complexity: O(1)
# (Only a few variables are used, no extra data structure.)           


