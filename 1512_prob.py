# 1512. Number of Good Pairs
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


#Brute Force

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(1+i,len(nums)):
                if nums[i]==nums[j]:
                    c+=1
        return c


# Time = O(n²) 
# Space = O(1)


# Optimised 

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        p=0
        mp={}
        for num in nums:
            if num in mp:
                p+=mp[num]
                mp[num]+=1
            else:
                mp[num]=1
        return p




        













# Time Complexity = O(n)
# Space Complexity = O(n)

        