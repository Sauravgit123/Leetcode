# 35. Search Insert Position
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


# This is brute force approach
a=[1,3,5,6]
target=7
for i in range(len(a)):
    if a[i]>=target:
        print(i)
        break
else:
    print(len(a))

# can be using binary search algorithm


nums = [1,3,5,6]
target = 5

lb=len(nums)
low=0
high=len(nums)-1
if low>high:
    print(-1)
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1
print(lb)

# Time Complexity: O(log n)
# Space Complexity: O(1)


                
        