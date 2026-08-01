# 1394. Find Lucky Integer in an Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

 

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
 

# Constraints:

# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500
 


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hp={}
        for i in arr:
            if i not in hp:
                hp[i]=1
            else:
                hp[i]+=1
        m=-1
        for i in hp:
            if i==hp[i]:
                m=max(m,i)
        return m


# Complexity
# Time: O(n)
# Making HashMap : O(n)
# Iterate hashmap: O(k), k = unique elements (k ≤ n)
# Overall: O(n)

# Auxiliary Space: O(n)
# In HashMap all elements can be stored (if distinct) -> worst case 
