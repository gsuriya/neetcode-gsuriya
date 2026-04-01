# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        c3 = dummy = ListNode(-1)
        carry = 0

        while c1 or c2 or carry:
            a = c1.val if c1 else 0
            b = c2.val if c2 else 0

            total = a + b + carry
            sum_ = total % 10
            carry = 1 if total >= 10 else 0

            c3.next = ListNode(sum_)
            c3 = c3.next

            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
        
        return dummy.next