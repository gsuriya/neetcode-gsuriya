# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return None

        # split into middle
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        c2 = slow.next
        slow.next = None
        c1 = head

        # reverse second list
        prev = None
        tmp = c2
        while c2:
            tmp = c2.next
            c2.next = prev
            prev = c2
            c2 = tmp
        c2 = prev

        # merge (c1 list will always be larger)
        c3 = dummy = ListNode(-1)
        
        while c1 and c2:
            c3.next = c1
            c1 = c1.next
            c3 = c3.next

            c3.next = c2
            c2 = c2.next
            c3 = c3.next
        
        if c1:
            c3.next = c1
        
        head = dummy.next

        