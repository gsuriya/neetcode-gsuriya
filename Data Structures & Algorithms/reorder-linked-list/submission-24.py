# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # edge case
        if not head or not head.next or not head.next.next:
            return None

        # split the whole LL into 2
        # find middle
        fast = head.next
        slow = head
    
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

        # merge the two LLs
        curr1 = head
        curr2 = head2

        curr3 = dummy = ListNode()

        count = 1
        while curr1 and curr2:
            if count == 1:
                curr3.next = curr1
                curr1 = curr1.next
                count = 2
            elif count == 2:
                curr3.next = curr2
                curr2 = curr2.next
                count = 1
            curr3 = curr3.next

        head = dummy.next

        # attach remainder curr1    
        if not curr2:
            curr3.next = curr1
        elif not curr1:
            curr3.next = curr2

        return None
            