# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # merge algo for LL

        c3 = dummy = ListNode(-1)
        c1, c2 = list1, list2

        # keep merging until 1 pointer reaches the end
        while c1 and c2:
            if c1.val <= c2.val:
                c3.next = c1
                c1 = c1.next
            else:
                c3.next = c2
                c2 = c2.next
            c3 = c3.next

        # attach the rest
        if c1:
            c3.next = c1
        elif c2:
            c3.next = c2

        return dummy.next

