# 40. Combination Sum II
# Medium
# Topics
# premium lock icon
# Companies
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30



res=[]
k=8
def solve(i,nums,temp,t):
    if t==k:
        res.append((temp.copy()))
        return
    if t>k or i>=len(nums):
        return
    
    for j in range(i,len(nums)):
        if nums[j]==nums[j-1] and j>i:
            continue
        temp.append(nums[j])
        solve(j+1,nums,temp,t+nums[j])
        temp.pop()
    return res
       


nums=[10,1,2,7,6,1,5]
nums.sort()
print(solve(0,nums,[],0))

# Time: O(2^N)  (worst case)
# Space: O(N)   (recursion stack)
