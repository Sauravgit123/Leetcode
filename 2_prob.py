# 2. Add Two Numbers
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1=l1
        c2=l2
        ans=ListNode(-1)
        t=ans
        c=0
        while c1 or c2 or c:
            a=0
            b=0
            if c1:
                a=c1.val
            if c2:
                b=c2.val 
            to=a+b+c
            d=to%10
            c=to//10
            t.next=ListNode(d)
            t=t.next
            if c1:
                c1=c1.next
            if c2:
                c2=c2.next
        return ans.next


# Complexity:
# Time: O(max(n, m))
# Space: O(max(n, m)) 