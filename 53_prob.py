# 53. Maximum Subarray
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.





# nums = [5,4,-1,7,8]
# maxi=float("-inf")
# n=len(nums)
# for i in range(n):
#     t=0
#     for j in range(i,n):
#         t+=nums[j]
#         maxi=max(t,maxi)
# print(maxi)

# Brute-Force Method 
# Time: O(n²)
# Space: O(1)



# OPTIMAL SOLUTION   Kadane's Algorithm

nums = [5,4,-1,7,8]
maxi=float("-inf")
n=len(nums)
t=0
for i in range(n):
    t+=nums[i]
    maxi=max(maxi,t)
    if t<0:
        t=0
print(maxi)

# Time: O(n) (only 1 traversal)
# Space: O(1)











