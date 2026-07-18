# 441. Arranging Coins
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You have n coins and you want to build a staircase with these coins. 
# The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1
 
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        for i in range(1,n+1):
            if n>=i:          
                n-=i
            else:          
                return i-1
        return i

# Time Complexity: O(√n)
# Space Complexity: O(1)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Binary Search range
        low = 0
        high = n

        # Stores the maximum complete rows found so far
        ans = 0

        while low <= high:

            # Find middle row count
            mid = (low + high) // 2

            # Total coins needed to build 'mid' complete rows
            coins = mid * (mid + 1) // 2

            # If we have enough coins
            if coins <= n:
                ans = mid          # mid is a valid answer
                low = mid + 1      # Try to build more rows

            # Not enough coins
            else:
                high = mid - 1     # Search in the left half

        return ans

# Complexity
# Time Complexity: O(log n)
# Space Complexity: O(1)




                
            
