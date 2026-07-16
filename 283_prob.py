# 283. Move Zeroes
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?


# nums = [0,1,0,3,0,7,0,12]


# k=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[k]=nums[i]
#         k+=1

# while k<len(nums):
#     nums[k]=0
#     k+=1
# print(nums)




# optimal sol


nums = [0,1,0,3,0,7,0,12]
if len(nums)==1:
    print(nums)
else:
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
                
    print(nums)
