# 342. Power of Four
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False

#         while n % 4 == 0:
#             n //= 4

#         return n == 1



def solve(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    return solve(n // 4)


# Time Complexity = O(log₄ n)
# Space Complexity = O(log₄ n) (recursion stack)





class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1


# Time: O(log₄ n)
# Space: O(1)


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and 1073741824 % n == 0


# Time = O(1)
# Space = O(1)