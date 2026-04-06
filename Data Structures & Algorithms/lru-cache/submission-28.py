class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    """

    remove the LRU key --> ordering of the keys
    hashmap with ordered keys
    linked list that acts like a stack/queue

    """
    def __init__(self, capacity: int):
        """
        initialize capacity
        empty map
        doubly linked list MRU <-> LRU
        """

        self.key_to_node = {} # key --> node
        self.capacity = capacity
        self.size = 0

        self.MRU = ListNode(-1, -1)
        self.LRU = ListNode(-1, -1)
        self.MRU.next, self.LRU.prev = self.LRU, self.MRU


    def get(self, key: int) -> int:
        """
        move val node to MRU
        return map[key].val
        """
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.detach(node)
        self.attach(node)
        return node.val

        
    def put(self, key: int, value: int) -> None:
        """
        if key not in map:
            create k-v pair in map & node
            move node to MRU

            if capacity reached --> remove LRU, delete k-v from map
        
        else key in map --> js update the val
            map[key] = value 
            move to MRU
        """

        if key not in self.key_to_node:
            node = ListNode(value, key)
            self.size += 1
            self.key_to_node[key] = node
            self.attach(node)

            if self.size > self.capacity:
                nodeR = self.LRU.prev
                self.detach(nodeR)
                del self.key_to_node[nodeR.key]
                self.size -= 1
        
        else:
            node = self.key_to_node[key]
            node.val = value
            self.detach(node)
            self.attach(node)

    """
    
    PREV

    MRU
    |     1
    3
    |
    4
    |
    LRU

    NEXT

    """        

    # attaches to MRU
    def attach(self, node):
        node.next = self.MRU.next
        node.prev = self.MRU
        self.MRU.next = node
        node.next.prev = node

    # detach
    def detach(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


        
