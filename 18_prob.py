# 18. 4Sum
# Medium
# Topics
# premium lock icon
# Companies
# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        ans = []

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quad = sorted([nums[i], nums[j], nums[k], nums[l]])

                            if quad not in ans:
                                ans.append(quad)

        return ans
    
# Time: O(n⁴)
# Space: O(k) for storing unique quadruplets.


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        st = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()

                for k in range(j + 1, n):
                    x = target - (nums[i] + nums[j] + nums[k])

                    if x in seen:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], x]))
                        st.add(quad)

                    seen.add(nums[k])

        return [list(x) for x in st]
    

# Time Complexity
# Outer loops (i, j): O(n²)
# Inner loop (k): O(n)
# Hash lookup: O(1)

# Overall: O(n³)

# Space Complexity
# seen: O(n)
# Result set: O(k) (unique quadruplets)

# Auxiliary Space: O(n)