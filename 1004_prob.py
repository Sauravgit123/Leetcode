# 1004. Max Consecutive Ones III
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


# BRUTE FORCE 

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
maxi=0

for i in range(len(nums)):
    z=0
    for j in range(i,len(nums)):
        if nums[j]==0:
            z+=1
            if z>k:
                break
        maxi=max(maxi,j-i+1)
print(maxi)


# Complexity
# Time: O(n²)
# Space: O(1)


# BETTER APPROACH

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
maxi=0
l=0
r=0
z=0
while r<len(nums):
    if nums[r]==0:
        z+=1
    while z>k:            # |  IN VALID SO SHIFT LEFT POINTER TO MAKE IT VALID
        if nums[l]==0:    # |
            z-=1          # |
        l+=1              # |
    maxi=max(maxi,r-l+1)
    r+=1
    
print(maxi)

# Complexity
# Time: O(n)
# Space: O(1)



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r=0,0
        z=0
        maxi=0
        while r<len(nums):
            if nums[r]==0:
                z+=1
            if z>k:          
                if nums[l]==0: 
                    z-=1                    # Shrink window by 1 if zeros exceed k  
                l+=1
            if z<=k:
                maxi=max(maxi,r-l+1)                   # Updating  answer for valid window
            r+=1
        return maxi


# Complexity:
# Time: O(2n) = O(n)
# Space: O(1)



#OPTIMAL 
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        m=0
        l=0
        r=0
        d={}
        while r<len(fruits):
            d[fruits[r]]=d.get(fruits[r],0)+1
            if len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
    
            if len(d)<=2:
                m=max(m,r-l+1)
            r+=1
        return m
            
                
                
                

