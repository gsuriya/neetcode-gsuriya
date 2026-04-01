"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(N^2) algo
        # 1. create base list
        # 2. for every curr2 node, find random val associated w/ curr1
        # 3. Find the node w/ that random val in the 2nd LL
        # 4. Set curr2.random = node w/ random val in 2nd LL
        
        curr = head
        curr2 = dummy = Node(-1)
        while curr:
            curr2.next = Node(curr.val)
            curr = curr.next
            curr2 = curr2.next
        
        curr2 = dummy.next
        curr = head
        while curr2:
            if curr.random == None or curr.random.val == None:
                curr2.random = None
            else:
                random_loc = self.find(dummy, curr.random.val)
                curr2.random = random_loc
            curr2 = curr2.next
            curr = curr.next
        
        return dummy.next
    
    def find(self, dummy, val):
        curr = dummy.next
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return curr

