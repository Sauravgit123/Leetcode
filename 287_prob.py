# 287. Find the Duplicate Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?



# Space not optimal
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}

        for n in nums:
            d[n]=d.get(n,0)+1
        
        for val in d:
            if d[val]>1:
                return val

# Complexity
# Time: O(n) 
# Space: O(n)


# WITH SPACE OPTIMALITY

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=nums[0]
        f=nums[nums[0]]

        while s!=f:
            s=nums[s]
            f=nums[nums[f]]
        
        s=0

        while s!=f:
            s=nums[s]
            f=nums[f]
        
        return s
         
# Complexity
# Time: O(n) 
# Space: O(1)