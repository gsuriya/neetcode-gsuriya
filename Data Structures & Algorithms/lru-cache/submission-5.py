class ListNode:
    def __init__(self, val, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.LRU_map = {}
        self.LRU, self.MRU = ListNode(-1), ListNode(-1)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.LRU_map:
            # move node to MRU (bottom of stack)
            self.disconnect_node(self.LRU_map[key])
            self.move_to_MRU(self.LRU_map[key])
            # return val for key
            return self.LRU_map[key].val
        else:
            return -1
       
    def put(self, key: int, value: int) -> None:
        if key in self.LRU_map:
            # move node to MRU (bottom of stack)
            self.disconnect_node(self.LRU_map[key])
            self.move_to_MRU(self.LRU_map[key])
            # update key w/ valz
            self.LRU_map[key].val = value
        else:
            # create and move new node to MRU (bottom of stack)
            self.LRU_map[key] = ListNode(val=value, key=key)
            self.move_to_MRU(self.LRU_map[key])

            # increment size
            self.size += 1

            # if over capacity, delete head node
            if self.size > self.capacity:
                curr = self.LRU.next
                self.disconnect_node(curr)

                # delete key of LRU from map
                del self.LRU_map[curr.key]
                self.size -= 1

    # moves node to MRU (bottom of stack)
    def disconnect_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def move_to_MRU(self, node):
        node.next = self.MRU
        node.prev = self.MRU.prev
        self.MRU.prev = node
        node.prev.next = node
        
        
