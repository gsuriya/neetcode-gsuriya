class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = None


class LRUCache:
    """

    evicts the least recently used one
    queue/stack but need to be able to move elems from middle to top in O(1)
    --> doubly linked list

            prev

              MRU

        k -->  v

        k -->  v

              LRU

            next

    """
    def __init__(self, capacity: int):
        # have 2 dummy nodes on each side to easily remove lru and and add to mru side
        # instantiate capacity and current size
        self.MRU = ListNode(-1)
        self.LRU = ListNode(-1)
        self.MRU.next, self.LRU.prev = self.LRU, self.MRU

        self.capacity = capacity
        self.size = 0

        self.key_to_node = {} # key --> node

    def get(self, key: int) -> int:
        # if key doesn't exist, return -1
        if key not in self.key_to_node:
            return -1
        
        # move val to MRU
        node = self.key_to_node[key]
        self.detach(node)
        self.attach(node)
        
        # return val
        return node.val

    def put(self, key: int, value: int) -> None:
        # update K-V if key exists, add to MRU
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.detach(node)
            self.attach(node)

        # create it if it doesn't exist, and add to MRU
        else:
            node = ListNode(value)
            node.key = key
            self.key_to_node[key] = node
            self.attach(node)
            
            # if capacity is exceeded, evict from LRU side
            self.size += 1
            if self.size > self.capacity:
                node = self.LRU.prev
                self.detach(node)
                # get rid of key->node mapping now
                del self.key_to_node[node.key]
    
    """
    prev                next



    MRU -> <- node -> <- LRU


    """

    # detaching from middle or LRU
    def detach(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None
    
    # only attaching to MRU
    def attach(self, node):
        node.prev = self.MRU
        node.next = self.MRU.next
        self.MRU.next.prev = node
        self.MRU.next = node

        
