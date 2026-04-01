# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse LL
        curr = tmp = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tail = prev

        # delete node
        curr = tail
        # - single node
        if not curr.next:
            return None
        # - multiple nodes
        elif n == 1:
            tail = tail.next
        else:
            count = 1
            while curr and count < n-1:
                count += 1
                curr = curr.next
            curr.next = curr.next.next

        # reverse LL, return head
        curr = tmp = tail
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head = prev
        return head