# 328. Odd Even Linked List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, group all the nodes with odd indices
#  together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
 

# Constraints:

# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106



class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        odd = []
        even = []

        curr = head
        index = 1

        while curr:
            if index % 2 == 1:
                odd.append(curr.val)
            else:
                even.append(curr.val)

            curr = curr.next
            index += 1

        arr = odd + even

        curr = head
        i = 0

        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1

        return head

# Time Complexity:
# First traversal = O(n)
# Second traversal = O(n)
# Total:O(n)

# Space Complexity:O(n) because we used odd and even arrays.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        o=head
        e=head.next
        eh=e
        while e and e.next:
            o.next=o.next.next
            e.next=e.next.next
            o=o.next
            e=e.next
        o.next=eh
        return head


# Complexity:
# Time: O(n)
# Space:O(1)