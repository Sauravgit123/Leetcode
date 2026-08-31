# 92. Reverse Linked List II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
 

# Follow up: Could you do it in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        c=head
        p=1

        while p<left-1:
            c=c.next
            p+=1

        if left==1:
            bef=None
            temp=head
        else:
            bef=c
            temp=c.next
        d=0
        x=right-left
        pr=None
        ln=temp
        while d<=x:
            fr=temp.next
            temp.next=pr
            pr=temp
            temp=fr
            d+=1

        if bef:
            bef.next=pr
        
        else:
            head=pr
        
        ln.next=temp
        return head
    
# Time: O(n)
# Space: O(1)  
        


        
        

        