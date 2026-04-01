# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the LL in half, first half bigger
        slow = c1 = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        c2 = slow.next
        slow.next = None

        # reverse the second LL
        tmp = c2
        prev = None
        while c2:
            tmp = c2.next
            c2.next = prev
            prev = c2
            c2 = tmp
        c2 = prev

        # dummy node, merge 2 lists (one node from each one)
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
