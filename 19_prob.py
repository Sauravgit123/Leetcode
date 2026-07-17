














# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        l=0
        while curr:
            curr=curr.next
            l+=1
        curr=head
        if l == n:
            return head.next      #Edge case when l==n
        for _ in range(l-n-1):
            curr=curr.next
        curr.next=curr.next.next
        return heada

# Complexity:
# Time:O(n)
# (Length traversal + second traversal)

# Space:O(1)









# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        fr=head
        bk=head
        for _ in range(n):
            fr=fr.next
        if fr==None:
            return head.next
        while fr.next:
            bk=bk.next
            fr=fr.next
        bk.next=bk.next.next
        return head



# Complexity
# Time: O(n) (one pass after the initial n-step advance)
# Space: O(1)


