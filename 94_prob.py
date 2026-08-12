# 94. Binary Tree Inorder Traversal
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)      
            res.append(root.val)    
            inorder(root.right)     
        inorder(root)
        return res

# Complexity
# Time: O(n)
# Space: O(h) (recursion stack)


# ITERATIVE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []
        curr = root
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            res.append(curr.val)
            curr = curr.right
        return res

# Complexity
# Time: O(n) (every node pushed & popped once)
# Space: O(n) (worst case stack)


