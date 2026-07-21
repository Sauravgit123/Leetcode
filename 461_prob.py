# 461. Hamming Distance
# Easy
# Topics
# premium lock icon
# Companies
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1
 

# Constraints:

# 0 <= x, y <= 231 - 1
 

# Note: This question is the same as 2220: Minimum Bit Flips to Convert Number.





# Hamming Distance is the number of positions where the corresponding bits of two numbers are different.
# Example 1
# x = 1  -> 0001
# y = 4  -> 0100

# Compare the bits:

# 0001
# 0100
# ----
# 0101

# There are 2 different bits, so the Hamming Distance = 2.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n=x^y
        c=0
        
        while n:
            n&=(n-1)
            c+=1
        return c

# Time Complexity
# Time = O(k)  - removes k set bits
# Space = O(1)