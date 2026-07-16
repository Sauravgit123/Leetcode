# 876. Middle of the Linked List
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        c=0
        while curr:
            curr=curr.next
            c+=1
        n=c
        mid=n//2
        curr=head
        for _ in range(mid):
            curr=curr.next
        return ans


# Time Complexity
# First traversal: O(n)
# Second traversal: O(n)
# Overall: O(n)

# Space Complexity
# O(1)



# The Tortoise-Hare Approach (also called the Slow and Fast Pointer technique) is a very common Linked List algorithm.

# Idea
# Tortoise (Slow Pointer) → moves 1 step at a time.
# Hare (Fast Pointer) → moves 2 steps at a time.

# slow → 1 step
# fast → 2 steps





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f=head
        s=head
        while f is not None and f.next is not None:
            s=s.next
            f=f.next.next
        return s

    


# Complexity
# Time Complexity: O(n)
# Space Complexity: O(1)

# Both have the same asymptotic complexity (O(n) time and O(1) space),but the slow-fast
# pointer approach is more efficient in practice because it finds the middle in a single
# traversal instead of two. It performs fewer operations (better constant factor), 
# which makes it faster even though the Big-O notation is the same.