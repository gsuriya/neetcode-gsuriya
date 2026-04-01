# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c1 = dummy = ListNode(-1, head)
        c2 = head

        # .next c2 by n
        while n > 0:
            c2 = c2.next
            n -= 1
        
        # move both until c2 @ end
        while c2:
            c1 = c1.next
            c2 = c2.next

        # delete using c1
        c1.next = c1.next.next

        return dummy.next


        