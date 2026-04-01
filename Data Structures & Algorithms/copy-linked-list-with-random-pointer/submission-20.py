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
        LL_map = {None: None} # node --> node

        # first pass: create duplicate nodes and add to map (no .next .random connections)
        curr = head
        while curr:
            LL_map[curr] = Node(curr.val)
            curr = curr.next

        # second pass: use LL_map to create the connetions
        curr = head
        while curr:
            LL_map[curr].next = LL_map[curr.next]
            LL_map[curr].random = LL_map[curr.random]
            curr = curr.next
        
        return LL_map[head]
        