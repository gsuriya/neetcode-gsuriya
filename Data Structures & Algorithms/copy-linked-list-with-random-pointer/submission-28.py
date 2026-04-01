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

        create nodes first (map old -> new)
        set pointers

old     3 -> 7 -> 4 -> 5 
        |    |    |    |
new     3    7    4    5

        """

        old_to_new = {None: None} # None None edge case

        # create nodes and old->new mapping
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        
        # add connections
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new[curr.next]
            old_to_new[curr].random = old_to_new[curr.random]
            
            curr = curr.next
        
        return old_to_new[head]






