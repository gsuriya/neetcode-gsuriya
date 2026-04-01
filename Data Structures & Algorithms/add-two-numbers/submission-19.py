# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        move both pointers across entire list

        # calculate sum and carry

        total = c1.val + c2.val # 11
        if total >= 10:
            sum = total % 10
            carry = 1 if total >= 10 else 0

        # the carry should go into next iteration/calculation

        c3.next = sum

        edge case: create new node if enough nodes (ex. 7 + 9)

        """

        c1 = l1
        c2 = l2
        c3 = dummy = ListNode(-1)

        sum_ = 0
        carry = 0
        while c1 or c2 or carry:
            # calc sum and carry
            a = c1.val if c1 else 0
            b = c2.val if c2 else 0

            total = a + b + carry # carry from last iteration
            sum_ = total % 10
            carry = 1 if total >= 10 else 0 

            # connect next node
            c3.next = ListNode(sum_)

            # move pointers
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
            c3 = c3.next
        
        return dummy.next

        