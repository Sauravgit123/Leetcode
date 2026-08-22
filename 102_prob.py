# 102. Binary Tree Level Order Traversal
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res= []
        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return res


# Complexity
# DFS (Recursive)
# Time - O(n)
# Space - O(n)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans

    
# BFS (Iterative)	
# Time - O(n)
# Space - O(n)


