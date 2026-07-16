# 448. Find All Numbers Disappeared in an Array
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums of n integers where nums[i] is in the range [1, n],
#  return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? 
# You may assume the returned list does not count as extra space.

# nums = [4,3,2,7,8,2,3,1]

# n=len(nums)
# new=[]
# for i in range(1,n+1):
#     if i not in nums:
#         new.append(i)
# print(new)


# Time : 
# O(n × n) = O(n²)

# Space:
# O(k) (k missing values  -- due to new list)


a = [4,3,2,7,8,2,3,1]

n=len(a)

for i in range(n):

    while n>=a[i]>=1 and a[i]!=a[a[i]-1]:
        ii=a[i]-1
        a[i],a[ii]=a[ii],a[i]

for i in range(n):
    if a[i]!=i+1:
        print(i+1)



# Complexity
# Time: O(n)
# Extra Space: O(1) (returned list  no new extra space )  as assumed in ques










