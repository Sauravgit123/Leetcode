# 1380. Lucky Numbers in a Matrix
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an m x n matrix of distinct numbers, return all lucky 
# numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the 
# minimum element in its row and maximum in its column.

 

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the 
# minimum in its row and the maximum in its column.
# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the 
# minimum in its row and the maximum in its column.
# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the 
# minimum in its row and the maximum in its column.
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 105.
# All elements in the matrix are distinct.


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        rows = []
        col = []

        for i in range(m):
            rows.append(min(matrix[i]))
        for i in range(n):
            maxi = float("-inf")
            for j in range(m):
                if maxi<matrix[j][i]:
                    maxi=matrix[j][i]
            col.append(maxi)
        
        return list(set(rows) & set(col))
    

# Time: O(m × n)
# Space: O(m + n)



class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        for i in range(m):
            mini = min(matrix[i])
            col = matrix[i].index(mini)

            flag = True
            for j in range(m):
                if matrix[j][col] > mini:
                    flag = False
                    break

            if flag:
                ans.append(mini)

        return ans
    
# Complexity
# Time: O(m × n)
# Space: O(1) (excluding the output list)