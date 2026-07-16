# 128. Longest Consecutive Sequence
# Medium
# Topics
# premium lock icon
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


# nums = [1,2,3,4]
# n=len(nums)
# s=set(nums)
# maxi=0
# for i in range(n):
#     c=1   
#     num=nums[i] 
#     while num+1 in s:
#         c+=1
#         num+=1
#     maxi=max(maxi,c)
# print(max(c,maxi))

# Time Complexity: O(n²)
# Space Complexity: O(n)



#More Efficient

# nums = [1,2,3,4]
# nums.sort()
# n=len(nums)
# l=0
# c=0
# s=float("-inf")
# for i in range(n):
#     num=nums[i]
#     if num-1 ==s:
#         c+=1
#         s=num

#     elif (num-1)!=s:
#         c=1
#         s=num
#     l=max(c,l)
# print(l)
    
# Time Complexity: O(n log n) due to sorting, followed by an O(n) traversal.
# Space Complexity: O(1) auxiliary space (ignoring Python's internal sort implementation details).





# Optimal Solution

nums = [1,2,-1,3,4]
s=set(nums)
n=len(nums)
lo=0
for num in s:
    if num-1 not in s:
        c=1
        while num+1 in s:
            c+=1
            num+=1
        lo=(max(lo,c))
print(lo)



# Time Complexity: O(n), since each element is visited at most once.
# Space Complexity: O(n), due to the hash set storing all unique elements.






