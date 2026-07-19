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

            # Include current element
            temp.append(nums[i])
            solve(i + 1, temp)

            # Backtrack
            temp.pop()

            # Exclude current element
            solve(i + 1, temp)

        solve(0, [])
        return ans

# Time Complexity : O(n × 2ⁿ)
# Space Complexity : O(n × 2ⁿ)
#                    (Answer storage dominates)

# Auxiliary Space (excluding output): O(n)
#                    (Recursion stack)