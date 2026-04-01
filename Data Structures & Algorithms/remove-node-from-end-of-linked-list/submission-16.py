# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # start L at dummy node
        # start R at head
        L = dummy = ListNode(-1, head)
        R = head

        # move R by n spaces
        while n > 0:
            R = R.next
            n -=1

        # move L and R at same speed until R null
        while R:
            R = R.next
            L = L.next

        # delete node using L
        L.next = L.next.next

        # return head
        return dummy.next