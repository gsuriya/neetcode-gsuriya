from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return  

        # 1️⃣ Find the middle of the list (slow will be at mid)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2️⃣ Reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None  # 🔥 Disconnect first half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 3️⃣ Merge two halves (without a dummy node)
        first, second = head, prev  # first -> beginning, second -> reversed half
        while second:
            temp1, temp2 = first.next, second.next  # Save next pointers
            first.next = second  # Connect first half node to second half node
            second.next = temp1  # Connect second half node to next first half node
            first, second = temp1, temp2  # Move pointers forward