# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(-1, head)
        curr = prev = tmp = kth = None

        while True:
            # move kth, if can't --> done reversing
            kth = self.move_kth(groupPrev, k)
            if not kth:
                return dummy.next

            # intialize reversal pointers
            curr = tmp = groupPrev.next
            prev = kth.next
            stop = kth.next

            while curr != stop:
                tmp = tmp.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
    
    def move_kth(self, start, k):
        curr = start
        while curr and k:
            curr = curr.next
            k -= 1
        return curr


        