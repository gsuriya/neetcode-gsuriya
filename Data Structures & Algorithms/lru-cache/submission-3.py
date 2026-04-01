class ListNode:
    def __init__(self, val, key=None):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

"""
oml im the goat
only mistake was that i forgot to delete hashmap k-v pair when deleting LRU node
"""


# bro this question is a QUEUE is neetcode retarded?
class LRUCache:
    # 13:43 in video
    def __init__(self, capacity: int):
        # initialize key-val data structure w/ maxcapacity
        self.key_to_node = {} # map: key --> node w/ val
        self.max_capacity = capacity

        self.dummy_head = ListNode(-1) # dummy node for start, don't have to handle moving head
        self.dummy_tail = ListNode(-1) # access node at the top 

        # connect head and tail
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    """
    2 helper functions for doubly linked list
    1. insert at tail
    2. remove from middle
    """
    def insert_at_tail(self, curr):
        curr.prev = self.dummy_tail.prev
        self.dummy_tail.prev.next = curr
        curr.next = self.dummy_tail
        self.dummy_tail.prev = curr

    def remove_from_middle(self, curr):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.prev, curr.next = None, None

    def get(self, key: int) -> int:
        # if key doesn't exist, return -1
        if key not in self.key_to_node:
            return -1

        # if key exists
        else:
            # - move node to tail end b/c its most recently used
            # - THEN return node.val
            curr = self.key_to_node[key]
            self.remove_from_middle(curr)
            self.insert_at_tail(curr)
            return curr.val

    def put(self, key: int, value: int) -> None:
        # if key doesn't exist, add k-v pair
        # - insert node at tail, add key to hashmap
        if key not in self.key_to_node:
            # k-v pair to map
            curr = ListNode(value, key)
            self.key_to_node[key] = curr
            # insert node at tail
            self.insert_at_tail(curr)

        # if key exists, update key-val w/ new val
        # - move node to tail end b/c its most recently used
        else:
            self.key_to_node[key].val = value
            curr = self.key_to_node[key]
            self.remove_from_middle(curr)
            self.insert_at_tail(curr)

        # once added, if capacity > max_capacity, remove LRU k-v pair
        # - remove head
        if len(self.key_to_node) > self.max_capacity:
            curr = self.dummy_head.next
            del self.key_to_node[curr.key]
            self.remove_from_middle(curr)

