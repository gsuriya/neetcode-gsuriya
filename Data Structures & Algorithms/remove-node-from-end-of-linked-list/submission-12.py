# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L = dummy = ListNode(-1, head)
        R = head

        # move R to correct starting location
        while n > 0:
            R = R.next
            n -= 1

        # move both at same speed
        while R:
            R = R.next
            L = L.next
        
        L.next = L.next.next

        return dummy.next