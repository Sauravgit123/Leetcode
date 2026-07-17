# 21. Merge Two Sorted Lists
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be 
# made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            d=ListNode(-1)
            curr=d
            l1=list1
            l2=list2

            while l1 and l2:
                if l1.val>l2.val:
                    curr.next=l2
                    curr=curr.next
                    l2=l2.next
                else:
                    curr.next=l1
                    curr=curr.next
                    l1=l1.next
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            return d.next  #as d is -1 ..(with the help of dummy pointer)


# Complexity
# Time: O(n + m)
# Space: O(1)

# (n = list1 length, m = list2 length)

        