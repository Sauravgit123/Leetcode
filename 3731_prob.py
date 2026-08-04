# 3731. Find Missing Elements
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums consisting of unique integers.

# Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

# The smallest and largest integers of the original range are still present in nums.

# Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.

# Example 1:
# Input: nums = [1,4,2,5]
# Output: [3]
# Explanation:
# The smallest integer is 1 and the largest is 5, so the full range should be [1,2,3,4,5]. Among these, only 3 is missing.

# Example 2:
# Input: nums = [7,8,6,9]
# Output: []
# Explanation:
# The smallest integer is 6 and the largest is 9, so the full range is [6,7,8,9]. All integers are already present, so no integer is missing.

# Example 3:
# Input: nums = [5,1]
# Output: [2,3,4]
# Explanation:
# The smallest integer is 1 and the largest is 5, so the full range should be [1,2,3,4,5]. The missing integers are 2, 3, and 4.

# Constraints:
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 100

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        s=set(nums)
        for i in range(nums[0],nums[-1]):
            if i not in s:
                ans.append(i)
        return ans
                

# Complexity
# nums.sort() → O(n log n)
# set(nums) → O(n)
# Loop → O(m), jahan m = nums[-1] - nums[0]
# i not in s → O(1) average
# Overall Time Complexity: O(n log n + m)

# Space Complexity: O(n) (set)

                

        