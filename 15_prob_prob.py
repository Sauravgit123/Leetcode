
# 15. 3Sum
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return all the triplets [nums[i], nums[j], 
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105






nums = [-1,0,1,2,-1,-4]

n=len(nums)
ans=[]

i=0
j=i+1
k=j+1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if nums[i]+nums[k]+nums[j]==0:
                t = sorted([nums[i], nums[j], nums[k]])
                if t not in ans:
                    ans.append(t)
print(ans)

# Time Complexity
# Three nested loops: O(n³)
# triplet not in ans takes O(m), where m is the number of triplets already in ans. In the worst case this can make the complexity O(n⁴).

# Worst-case Time Complexity: O(n⁴)

# Space Complexity
# Auxiliary Space: O(1) (ignoring the output list)
# Including output: O(k), where k is the number of unique triplets stored.




class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        st = set()

        for i in range(n):
            seen = set()

            for j in range(i + 1, n):
                k = -(nums[i] + nums[j])

                if k in seen:       
                    triplet = tuple(sorted([nums[i], nums[j], k]))
                    st.add(triplet)

                seen.add(nums[j])

        return [list(x) for x in st]
    
# Time Complexity
# Outer loop: O(n)
# Inner loop: O(n)
# Hash set lookup: O(1)

# Overall: O(n²)

# Space Complexity
# seen set: O(n)
# Result set: O(k) (for unique triplets)

# Auxiliary Space: O(n)




class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans=[]
        i=0
        
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while k>j:
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    ans.append([ nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while k>j and nums[j]==nums[j-1]:
                        j+=1
                    while k>j and nums[k]==nums[k+1]:
                        k-=1
        return ans
                    



# Complexity
# Time: O(n²)
# Sorting: O(n log n)
# Outer loop: O(n)
# Two pointers: O(n) for each i
#  Overall: O(n²)

# Space: O(1) (excluding the output list)



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j!=1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while l>k:
                    if nums[i]+nums[k]+nums[j]+nums[l]>target:
                        l-=1
                    elif nums[i]+nums[k]+nums[j]+nums[l]<target:
                        k+=1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while l>k and nums[k]==nums[k-1]:
                            k+=1
                        while l>k and nums[l]==nums[l+1]:
                            l-=1
        return ans


# Time Complexity: O(n³)
# Space Complexity: O(k), where k is the number of quadruplets stored in the answer.


