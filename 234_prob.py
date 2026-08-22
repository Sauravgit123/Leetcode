# 234. Palindrome Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=head
        f=head

        while f and f.next:
            s=s.next
            f=f.next.next
        if f:       # when no. of nodes is odd
            s=s.next
        
        pr=None
        temp=s

        while temp:
            fr=temp.next
            temp.next=pr
            pr=temp
            temp=fr
        sec=pr
        f=head

        while f and sec:
            if f.val==sec.val:
                f=f.next
                sec=sec.next
            else:
                return False
        return True

# Complexity
# Time: O(n)
# Middle find → O(n)
# Reverse → O(n)
# Compare → O(n)
# Overall → O(n)
# Space: O(1)