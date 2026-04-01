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
        """

        map: old node --> new node

        1. create new nodes (no connections)
        2. iterate through old structure, linking up new nodes

              c
        old:  0 -> None

        new:  0 -> None   


        """
        # edge case: map None nodes to None
        old_to_new = {None: None} # old node --> new node

        # create new nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # link up new nodes
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new[curr.next]
            old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]


