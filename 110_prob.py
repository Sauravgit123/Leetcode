# 110. Balanced Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a binary tree, determine if it is height-balanced.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff=0
        def check(node):
            if node==None:
                return 0
            
            l=check(node.left)
            r=check(node.right)
            self.diff=max(self.diff,abs(l-r))
            return 1+max(l,r)
        check(root)
        if self.diff > 1:
            return False
        else:
            return True
            
#Complexity :
# Time: O(n)
# Space: O(h)  h - height of tree



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff=0
        def check(node):
            if node==None:
                return 0
            
            l=check(node.left)
            if l ==-1 :
                return -1
            r=check(node.right)
            if r ==-1 :
                return -1
            if abs(l-r) > 1:
                return -1
            return 1+max(l,r)
        return check(root)!=-1

# normal → height return
# -1     → unbalanced signal

# Time: O(n) — every node visited once
# Space: O(h) — recursion stack, where h = tree height