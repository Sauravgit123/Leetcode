# 104. Maximum Depth of Binary Tree
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def h(node):

            if node==None:
                return 0

            l_h=h(node.left)
            r_h=h(node.right)
            return 1+max(l_h,r_h)
        
        return h(root)

# Time: O(n)
# Space: O(h) → recursion stack.


from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q=deque([])
        h=0
        q.append(root)
        while q:
            h+=1

            for i in range(len(q)):
                e=q.popleft()
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
        return h


# Complexity
# Time: O(n) — every node processed once
# Space: O(n) — queue can contain up to n nodes

