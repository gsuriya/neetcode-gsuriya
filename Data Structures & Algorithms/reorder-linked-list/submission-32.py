# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the LL
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None

        # reverse the second LL
        curr2 = tmp = head2
        prev = None
        while curr2:
            tmp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = tmp
        head2 = prev

        # merge
        curr1 = head
        curr2 = head2

        while curr1 and curr2:
            tmp1, tmp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr1, curr2, = tmp1, tmp2
        
        return None