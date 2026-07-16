# 141. Linked List Cycle
# Easy
# Topics
# premium lock icon
# Companies
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list 
# that can be reached again by continuously following the next pointer. Internally, 
# pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 
# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

# Follow up: Can you solve it using O(1) (i.e. constant) memory?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        temp=head

        while temp:
            if temp in s:
                return True
            else:
                s.add(temp)
            temp=temp.next
        return False

# Time Complexity
# Time: O(n)
# Space: O(n)


# Approach 2: Floyd's Cycle Detection Algorithm (Tortoise and Hare)

# Theory:
# Instead of storing visited nodes in a HashSet, we use two pointers:
# - Slow Pointer (Tortoise): moves one node at a time.
# - Fast Pointer (Hare): moves two nodes at a time.

# If the linked list contains a cycle, the fast pointer will eventually catch up to the slow pointer, and both pointers will meet at the same node.

# If there is no cycle, the fast pointer (or fast.next) will become None, indicating that the linked list ends normally.

# This approach eliminates the need for extra memory, making it more space-efficient than the HashSet approach.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None




class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
            if s==f:
                return True
                
        return False

# Time Complexity: O(n)
# - Each node is visited at most a constant number of times.

# Space Complexity: O(1)
# - No extra data structure is used; only two pointers are maintained.