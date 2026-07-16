# 645. Set Mismatch
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You have a set of integers s, which originally contains all the numbers from 1 to n.
#  Unfortunately, due to some error, one of the numbers in s got duplicated to another number 
# in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104







#Brute Force method

# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         n=[]
#         r=[]
#         for i in range(len(nums)):
#             if nums[i]not in n:
#                 n.append(nums[i])
#             else:
#                 r.append(nums[i])
#                 r.append(sum(range(1, len(nums) + 1)) - sum(set(nums)))
#         return r
            

# Time Complexity = O(n^2)
# Space Complexity = O(n)


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = set()
        duplicate = -1

        # 1. Duplicate number dhoodho (O(n) time)
        for num in nums:
            if num in visited:
                duplicate = num
            visited.add(num)

        # 2. 1 se n tak ghoom kar missing number dhoodho
        missing = -1
        for i in range(1, len(nums) + 1):
            if i not in visited:
                missing = i
                break

        return [duplicate, missing]

# Time Complexity = O(n)
# Space Complexity = O(n) 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=set()                                                 #USE SET TO AVOID N2 COMPLEXITY
        r=[]
        for i in range(len(nums)):    
            if nums[i]not in n: 
                n.add(nums[i])
            else:
                r.append(nums[i])
        r.append(sum(range(1, len(nums) + 1)) - sum(n))
        return r