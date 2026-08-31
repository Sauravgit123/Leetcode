# 238. Product of Array Except Self
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return an array answer 
# such that answer[i] is equal to the product of 
# all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is 
# guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time 
# and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is 
# guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) 
# extra space complexity? (The output array does not count as extra space for space complexity analysis.)




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]
        r=[1]

        for i in range(1,len(nums)):
            l.append(l[-1]*nums[i-1])
        
        for j in range(len(nums)-2,-1,-1):
            r.append(r[-1]*nums[j+1])
        
        r.reverse()

        return list(map(lambda x,y:x*y,l,r))


# # Complexity
# # Time: O(n)
# # Space: O(n) — l, r, and output




# OPTIMAL SOLUTION
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        l=1
        for i in range(len(nums)):
            res[i]=l
            l*=nums[i]
        
        r=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=r
            r*=nums[j]
        
        return res

# Complexity
# Time: O(n)
# Extra Space: O(1) — ONLY res output array