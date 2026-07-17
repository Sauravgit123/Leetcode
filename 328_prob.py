












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