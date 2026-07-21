# 136. Single Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-empty array of integers nums, every element 
# appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime 
# complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for 
# one element which appears only once.



# Brute force

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n)==1:
                return n

# Time: O(n²) 
# Space: O(1)


#Better

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}

        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        for n in mp:
            if mp[n] == 1:
                return n
    # Time: O(n)
    # Space: O(n)



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0

        for n in nums:
            ans^=n

        return ans


# Complexity
# Time: O(n) 
# Space: O(1)


