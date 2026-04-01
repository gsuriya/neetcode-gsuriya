# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse
        curr = tmp = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tail = prev

        # delete (edges: 1 node, beginning -- move head)
        curr = tail
        if not curr.next: # 1 node
            return None
        elif n == 1: # deleting beginning
            tail = tail.next
        else: # deleting middle/end
            count = 1
            while curr and count < n-1:
                curr = curr.next
                count += 1
            curr.next = curr.next.next

        # reverse
        curr = tmp = tail
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev