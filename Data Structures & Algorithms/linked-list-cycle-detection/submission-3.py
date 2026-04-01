# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # return true if cycle
        # fast and slow pointer
        # return true if they intersect

        fast = slow = head

        while fast and fast.next: # b/c fast moves two steps
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True # has cycle

        return False
        