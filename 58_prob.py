# 59. Spiral Matrix II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a positive integer n, generate an n x n matrix 
# filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20
 


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix=[[0]*n for i in range(n)]
        top=0
        left=0
        right=len(matrix)-1
        bottom=len(matrix)-1
        c=1
        while left<=right and bottom>=top:
            for i in range(left,right+1):
                matrix[left][i]=c
                c+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][right]=c
                c+=1
            right-=1

            if  bottom>=top:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=c
                    c+=1
                bottom-=1
            if  left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=c
                    c+=1
                left+=1
        return matrix
            

# Complexity:

# Time: O(n²) 
# Space: O(n²) 


        
