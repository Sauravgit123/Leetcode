# 199. Binary Tree Right Side View
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]

# Explanation:



# Example 3:

# Input: root = [1,null,3]

# Output: [1,3]

# Example 4:

# Input: root = []

# Output: []

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque()
        q.append(root)
        res=[]
        while q:
            n=len(q)
            for i in range(n):
                e=q.popleft()

                if i==n-1:
                    res.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
        
        return res

# Complexity
# Time: O(n)
# Space: O(n)





# OPTIMAL (without using queue)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.res=[]

        def revpost(node,depth):
            if node==None:
                return
            if depth==len(self.res):
                self.res.append(node.val)
            revpost(node.right,depth+1)
            revpost(node.left,depth+1)
        revpost(root,0)
        return self.res


# Complexity
# Time: O(n) — every node once
# Space: O(h) — recursion stack
