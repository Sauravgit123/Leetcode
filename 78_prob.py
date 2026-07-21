# 78. Subsets
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def solve(i, temp):

            if i == len(nums):
                ans.append(temp.copy())
                return

            temp.append(nums[i])
            solve(i + 1, temp)

            # Backtrack
            temp.pop()
            solve(i + 1, temp)

        solve(0, [])
        return ans

# Time Complexity  : O(n × 2^n)
# Space Complexity : O(n × 2^n)
# Auxiliary Space  : O(n)   (Recursion Stack)



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ts=1<<n
        res=[]
        for i in range(ts):
            l=[]
            for j in range(n):
                if i & (1<<j)!=0:  # ith set bit 
                    l.append(nums[j])
            res.append(l)
        return res
    
# Time Complexity  : O(n × 2^n)
# Space Complexity : O(n × 2^n)
# Auxiliary Space  : O(1)