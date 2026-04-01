class ListNode: # double linked list node
    def __init__(self, val, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key # need the key so that when remove for LRU, u can remove k-v from hashmap

class LRUCache:
    """
    
    MRU: get/put called on it

    LRU: 

    capacity = 4

    LinkedList = [
        prev

        LRU
k   -->  v3
k   -->  v1
k   -->  v2
        MRU
    
        next
    ]

    criteria for data structure:
    - remove from anywhere and append to the end
    - key maps to value
    - track size

    """

    def __init__(self, capacity: int):
        self.key_to_node = {} # key --> node w/ val
        self.length = 0
        self.capacity = capacity

        # LRU and MRU nodes to handle head/tail remove edge case
        self.LRU = ListNode(-1)
        self.MRU = ListNode(-1)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU
        
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        # move this node up to MRU
        node = self.key_to_node[key]
        self.detach(node)
        self.attach(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # if key inside --> update
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.detach(self.key_to_node[key])# move to MRU
            self.attach(self.key_to_node[key])

        # if key NOT inside --> add new node
        else:
            node = ListNode(val=value, key=key)
            self.key_to_node[key] = node # add mapping
            self.attach(node) # attach to LL
            self.length += 1 # increment length
            
            # if capacity exceeded, remove LRU
            if self.length > self.capacity:
                del self.key_to_node[self.LRU.next.key] # remove mapping
                self.detach(self.LRU.next) # detach LL
                self.length -= 1


    def detach(self, node):
        # remove from LL and fill string hole together
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None,  None

    def attach(self, node): # to MRU
        node.next = self.MRU
        node.prev = self.MRU.prev
        self.MRU.prev.next = node
        self.MRU.prev = node
        















        
