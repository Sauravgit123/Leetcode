# 189. Rotate Array
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# # 0 <= k <= 105
 
# nums = [1,2,3,4,5,6,7]
# k=3
# a=nums[(len(nums)-k):(len(nums))]

# for i in range(len(nums)-3):
#     a.append(nums[i])
# print(a)




# Complexity of your current approach:
# Time: O(n)
# Space: O(n)



# using same array only

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k=k%len(nums)
#         nums[:] = nums[-k:] + nums[:-k]
#         print(nums) 




#    STILL Complexity of your current approach:
# Time: O(n)
# Space: O(n)




# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
# nums=[1,2,3,4,5,6,7]
# print("Prg array: ",nums)
# k=1
# k=k%len(nums)
# for _ in range(0,k):
#     e=nums.pop()
#     nums.insert(0,e)
           
# print("Rotated : ",nums)


# Complexity
# Time: O(n*k) (slow for big inputs)
# Space: O(1)




def rev(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1


nums=[1,2,3,4,5,6,7]
n=len(nums)
k=3
k=k%len(nums)
rev(nums,0,n-1)
rev(nums,0,k-1)
rev(nums,k,n-1)


print(nums)





#  Optimal approach:

# Time: O(n)
# Space: O(1)





