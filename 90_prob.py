# 90. Subsets II
# Attempted
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 
# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans=[]
        nums.sort()
        def bk(i,temp,nums):
            if i==len(nums):
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            bk(i+1,temp,nums)
            temp.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            bk(i+1,temp,nums)
        bk(0, [], nums)
        return ans
        

# Complexity:
# Time: O(2^n) (worst case)
# Space: O(n) recursion stack 