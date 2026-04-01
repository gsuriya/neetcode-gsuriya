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
        node_map = {} # node --> random node

        # iteration 1: build map and base list
        curr = head
        curr2 = dummy = Node(-1)
        while curr:
            node_map[curr] = curr.random
            curr2.next = Node(curr.val)
            curr = curr.next
            curr2 = curr2.next
        
        # iteration 2: use map & set each node.next to associated random
        curr2 = dummy.next
        curr = head
        while curr2:
            if node_map[curr] == None:
                curr2.random = None
            else:
                random_loc = self.find(dummy, node_map[curr].val)
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

