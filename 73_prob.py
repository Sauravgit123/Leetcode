# 73. Set Matrix Zeroes
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        def infinity(matrix ,r,c):          
            for i in range(m):
                if matrix[i][c]!=0:
                    matrix[i][c]=float("+inf")
            for j in range(n):
                if matrix[r][j]!=0:
                    matrix[r][j]=float("+inf")

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    infinity(matrix,i,j)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==float("+inf"):
                    matrix[i][j]=0
        return matrix












# Time Complexity: O(m × n × (m + n))
# Reason:
# You traverse the entire matrix (m × n), and whenever a 0 is found, the infinity() 
# function scans the entire row (n) and the entire column (m). Therefore, the worst-case time complexity is:
# O(m×n×(m+n))
  

# Space Complexity: O(1)
# Reason:
# No extra data structures are used. Only a few variables (m, n, i, j) are allocated, so the extra space remains constant.







matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

m=len(matrix)
n=len(matrix[0])

for i in range(m):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print("")

mm=[0]*m
nn=[0]*n
for i in range(m):
    for j in range(n):
        if matrix[i][j]==0:
            mm[i]=-1
            nn[j]=-1
for i in range(m):
    for j in range(n):
        if mm[i] == -1 or nn[j] == -1:
            matrix[i][j] = 0
    
print(matrix)


            
# Complexity
# Time Complexity: O(m × n)
# Space Complexity: O(m + n)