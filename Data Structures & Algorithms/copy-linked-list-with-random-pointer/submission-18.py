"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    ALWAYS DRY RUN CODE BEFORE SUBMITTING
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       # deep copy
        LL_map = {None: None}

        """
        map = {
            3: node(3)
            7: node(7)
            4: node(4)
            5: node(5)
            None: None
        }

        3 -> 7 -> 4 -> 5 -> null

        """

        # connect nodes in LL map
        curr = head
        while curr:
            LL_map[curr] = Node(curr.val)
            curr = curr.next

        # use LL_map to create new list
        for node in LL_map:
            if not node:
                continue
            LL_map[node].next = LL_map[node.next]
            LL_map[node].random = LL_map[node.random]

        return LL_map[head]
        