# 2574. Left and Right Sum Differences
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed integer array nums of size n.

# Define two arrays leftSum and rightSum where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

 

# Example 1:

# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
# Example 2:

# Input: nums = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 105


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]
        summ=0
        for i in range(len(nums)-1):
            summ+=nums[i]
            leftsum.append(summ)
        rsum=[]
        j=0
        total=sum(nums)
        while j < len(nums):
            total-=nums[j]
            rsum.append(total)
            j+=1
        ans=[]
        for i in range(len(rsum)):
            ans.append(abs(leftsum[i]-rsum[i]))
        return ans

# Time Complexity: O(n)
# leftsum: O(n)
# rsum: O(n)
# ans: O(n)
# Overall: O(n)

# Auxiliary Space: O(n)
# leftsum + rsum = O(n)
# Including output: O(n)
        

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        ans = []
        for num in nums:
            total -= num
            ans.append(abs(left - total))
            left += num
        return ans

# Complexity
# Time: O(n)
# Auxiliary Space: O(1) (only left and total variables; output array isn't counted)