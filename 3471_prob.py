# 3471. Find the Largest Almost Missing Integer
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums and an integer k.

# An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

# Return the largest almost missing integer from nums. If no such integer exists, return -1.

# A subarray is a contiguous sequence of elements within an array.
 

# Example 1:

# Input: nums = [3,9,2,1,7], k = 3

# Output: 7

# Explanation:

# 1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
# 2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
# 3 appears in 1 subarray of size 3: [3, 9, 2].
# 7 appears in 1 subarray of size 3: [2, 1, 7].
# 9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
# We return 7 since it is the largest integer that appears in exactly one subarray of size k.

# Example 2:

# Input: nums = [3,9,7,2,1,7], k = 4

# Output: 3

# Explanation:

# 1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
# 2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
# 3 appears in 1 subarray of size 4: [3, 9, 7, 2].
# 7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
# 9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
# We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

# Example 3:

# Input: nums = [0,0], k = 1

# Output: -1

# Explanation:

# There is no integer that appears in only one subarray of size 1.

 

# Constraints:

# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 1 <= k <= nums.length


# BRUTE FORCE 

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        di={}
        i=0
        j=k-1
        while j<len(nums):
            seen=set()
            for nu in nums[i:j+1]:
                seen.add(nu)
            
            for nu in seen:
                di[nu]=di.get(nu,0)+1
            i+=1
            j+=1
        r=-1
        for nu in di:
            if di[nu]==1:
                r=max(r,nu)
        return r

# Time: O((n-k+1)-NO.OF WINDOWS POSSIBLE × k) ≈ O(nk)
# Space: O(k + n) ≈ O(n)




# OPTIMAL SOLUTION

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==n:
            return max(nums)
        else:
            di={}
            for nu in nums:
                di[nu]=di.get(nu,0)+1
            r=-1
            if k==1:
                for nu in di:
                    if di[nu]==1:
                        r=max(r,nu)
                return r
            else:
                if di[nums[0]]==1:
                    r=max(r,nums[0])
                if di[nums[n-1]]==1:
                    r=max(r,nums[n-1])
                return r


# Complexity:
# Time: O(n)
# Space: O(n)
