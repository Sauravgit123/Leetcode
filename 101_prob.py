# 101. Symmetric Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def sym(l,r):
            if not l and not r:
                return True
            
            if not l or not r:
                return False
            
            if l.val!=r.val:
                return False
            
            return sym(l.left,r.right) and sym(l.right,r.left)
        return sym(root.left,root.right)


# Complexity
# Time: O(n) — har node pair ko max ek baar check.
# Space: O(h) — recursion stack, where h is tree height.